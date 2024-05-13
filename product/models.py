from django.db import models
from accounts.models import User
from core.models import BaseModel
from django.utils.text import slugify
from core.utils import category_image_path, product_image_path
from django.urls import reverse

class Category(BaseModel):
    """
    Model representing a product category.

    Attributes:
        name (str): The name of the category.
        is_sub (bool): Indicates whether the category is a subcategory.
        description (str): Description of the category.
        slug (str): A unique slug for the category.
        image (ImageField): Image associated with the category.
        parent_category (ForeignKey): Parent category if this category is a subcategory.
    """
    name = models.CharField(max_length=255)
    is_sub = models.BooleanField(default=False)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to=category_image_path)
    parent_category = models.ForeignKey("self", on_delete=models.CASCADE , null=True , blank=True)
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    def save(self, *args, **kwargs):
        """
        Override the save method to set default values for slug and image.
        """
        if not self.image:
            self.image = 'path/to/default/image.jpg'
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """
        Get the absolute URL for the category.

        Returns:
            str: The absolute URL of the category.
        """
        if self.is_sub:
            return reverse("products", kwargs={"category_slug": self.parent_category.slug, "subcategory_slug": self.slug})
        else:
            return reverse("category", kwargs={"slug": self.slug})
        
    class Meta:
        verbose_name_plural = 'categories'
    
class Discount(BaseModel):
    """
    Model representing a discount.

    Attributes:
        type (str): Type of discount (e.g., percent, decimal).
        value (Decimal): Value of the discount.
        max_value (Decimal): Maximum value of the discount.
        is_active (bool): Indicates whether the discount is active.
        user (ManyToManyField): Users associated with the discount.
    """
    TYPE_OF_DISCOUNT = (
        ("percent", "Percent"),
        ("decimal", "Decimal"),
    )
    type = models.CharField(max_length=255,choices=TYPE_OF_DISCOUNT)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    max_value = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=False)
    user = models.ManyToManyField(User) # this relation is between staff and Discount not customer
    
    def __str__(self) -> str:
        return f"{self.type}"

class Product(BaseModel):
    """
    Model representing a product.

    Attributes:
        name (str): The name of the product.
        brand (str): The brand of the product.
        slug (str): A unique slug for the product.
        price (str): The price of the product.
        description (str): Description of the product.
        features (ManyToManyField): Features associated with the product.
        inventory_quantity (int): Inventory quantity of the product.
        image (ImageField): Image associated with the product.
        user_id (ForeignKey): User associated with the product.
        category_id (ForeignKey): Category associated with the product.
        discount_id (ForeignKey): Discount associated with the product.
    """
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    price = models.CharField(max_length=100)
    description = models.TextField()
    features = models.ManyToManyField("ProductFeature", through='ProductFeatureValue',blank=True)
    inventory_quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to=product_image_path)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name="products") # this relation is between staff and Product not customer
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    discount_id = models.ForeignKey(Discount, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self) -> str:
        return f'{self.name},{self.brand}'

    def save(self, *args, **kwargs):
        """
        Override the save method to set default values for slug and image.
        """
        if not self.image:
            self.image = 'path/to/default/image.jpg'
        if not self.slug:
            self.slug = slugify(self.brand + "-" + self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        """
        Get the absolute URL for the product.

        Returns:
            str: The absolute URL of the product.
        """
        return reverse("product_detail", kwargs={"pk": self.slug})
    
    class Meta:
        verbose_name_plural = 'products'

class ProductFeature(BaseModel):
    """
    Model representing a product feature.

    Attributes:
        name (str): The name of the feature.
    """
    name = models.CharField(max_length=255, help_text="like color")
    
    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        verbose_name_plural = 'features'    

class ProductFeatureValue(BaseModel):
    """
    Model representing the value of a product feature for a specific product.

    Attributes:
        value (str): The value of the feature.
        product (ForeignKey): The product associated with this feature value.
        feature (ForeignKey): The feature associated with this feature value.
    """
    value = models.CharField(max_length=255)    
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="products_feature_value")
    feature = models.ForeignKey(ProductFeature, on_delete=models.CASCADE,related_name="products_feature_value")
    
    def __str__(self) -> str:
        return f"{self.value} for {self.feature.name} in {self.product.name}"
    
    class Meta:
        verbose_name_plural = 'feature values'

class Comment(BaseModel):
    """
    Model representing a comment on a product.

    Attributes:
        text_message (str): The text of the comment.
        user_id (ForeignKey): User who posted the comment.
        product_id (ForeignKey): Product associated with the comment.
    """
    text_message = models.TextField(max_length = 500)
    user_id = models.ForeignKey(User , on_delete = models.CASCADE)
    product_id = models.ForeignKey(Product , on_delete = models.CASCADE)
    
class News(BaseModel):
    """
    Model representing a news item.

    Attributes:
        title (str): The title of the news.
        message_body (str): The body of the news message.
        create_by_user_id (ForeignKey): User who created the news.
        image (ImageField): Image associated with the news.
    """
    title = models.TextField(max_length = 100)
    message_body = models.TextField(max_length = 1000)
    create_by_user_id = models.ForeignKey(User , on_delete = models.PROTECT)
    image = models.ImageField()

