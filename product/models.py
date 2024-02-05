from django.db import models
from accounts.models import User
from core.models import BaseModel
from accounts.models import User
from core.utils import category_image_path, product_image_path


class Category(BaseModel):
    name = models.CharField(max_length=255)
    is_sub = models.BooleanField(default=False)
    image = models.ImageField(upload_to=category_image_path)
    parent_category = models.ForeignKey("self", on_delete=models.PROTECT , null=True , blank = True)
    discount = models.ForeignKey("Discount", on_delete=models.PROTECT, null=True, blank=True)
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    class Meta:
        verbose_name_plural = 'categories'
    


class Product(BaseModel):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    price = models.CharField(max_length=100)
    description = models.TextField()
    features = models.ManyToManyField("ProductFeature", through='ProductFeatureValue')
    inventory_quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to=product_image_path)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT) # this relation is between staff and Product not customer
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT)
    discount_id = models.ForeignKey("Discount", on_delete=models.PROTECT, null=True, blank=True)
    
    def __str__(self) -> str:
        return f'{self.name},{self.brand}'
    
    class Meta:
        verbose_name_plural = 'products'
        
class ProductFeature(BaseModel):
    name = models.CharField(max_length=255)
    text_value = models.TextField(blank=True, null=True)
    numeric_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    def __str__(self) -> str:
        return f"{self.name},{self.text_value}"
    
    class Meta:
        verbose_name_plural = 'features'


class ProductFeatureValue(BaseModel):
    value = models.CharField(max_length=255)    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    feature = models.ForeignKey(ProductFeature, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.value} for {self.feature.name} in {self.product.name}"
    
    class Meta:
        verbose_name_plural = 'feature values'

class Discount(BaseModel):
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
    
    
class Comment(BaseModel):
    text_message = models.TextField(max_length = 500)
    user_id = models.ForeignKey(User , on_delete = models.CASCADE)
    product_id = models.ForeignKey(Product , on_delete = models.CASCADE)
    
    
class News(BaseModel):
    title = models.TextField(max_length = 100)
    message_body = models.TextField(max_length = 1000)
    create_by_user_id = models.ForeignKey(User , on_delete = models.PROTECT)
    image = models.ImageField()

