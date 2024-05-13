from django.db import models
from core.models import BaseModel
from accounts.models import User
from product.models import Product

# Create your models here.

class Order(BaseModel):
    """
    Model representing an order made by a user.

    Attributes:
        total_price (Decimal): The total price of the order.
        is_paid (str): Indicates whether the order is paid or not.
        province (str): The province of the order's delivery address.
        city (str): The city of the order's delivery address.
        detailed_address (str): The detailed address of the order's delivery address.
        postal_code (int): The postal code of the order's delivery address.
        user (User): The user who made the order.
        coupon (Coupon): The coupon applied to the order.
    """
    PAYMENT_CHOICES = (
        ("Paid", True),
        ("Not Paid", False)
    )
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.CharField(max_length=25, choices=PAYMENT_CHOICES, default=False)
    province = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    detailed_address = models.TextField(blank=True, null=True)
    postal_code = models.PositiveIntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    coupon = models.ForeignKey("Coupon", on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self) -> str:
        return f"Total: {self.total_price}, Payment: {self.is_paid}"

    class Meta:
        verbose_name_plural = 'orders'


class OrderItem(BaseModel):
    """
    Model representing an item in an order.

    Attributes:
        quantity (int): The quantity of the product in the order.
        order (Order): The order to which the item belongs.
        product (Product): The product included in the item.
    """
    quantity = models.IntegerField()
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"number of {self.product.name}: {self.quantity}"

    class Meta:
        verbose_name_plural = 'order items'


class Cart(models.Model):
    """
    Model representing a shopping cart.

    Attributes:
        province (str): The province of the cart's delivery address.
        city (str): The city of the cart's delivery address.
        detailed_address (str): The detailed address of the cart's delivery address.
        postal_code (int): The postal code of the cart's delivery address.
        created_at (datetime): The date and time when the cart was created.
        updated_at (datetime): The date and time when the cart was last updated.
        user (User): The user who owns the cart.
    """
    province = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    detailed_address = models.TextField(blank=True, null=True)
    postal_code = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def calculate_total_price(self):
        """
        Calculate the total price of all items in the cart.

        Returns:
            Decimal: The total price of all items in the cart.
        """
        return sum(item.total_price() for item in self.cart_items.all())

    def __str__(self) -> str:
        return f"total cart: {self.calculate_total_price()}"

    class Meta:
        verbose_name_plural = 'carts'


class CartItem(models.Model):
    """
    Model representing an item in a shopping cart.

    Attributes:
        quantity (int): The quantity of the product in the cart.
        created_at (datetime): The date and time when the item was added to the cart.
        updated_at (datetime): The date and time when the item was last updated.
        cart (Cart): The cart to which the item belongs.
        product (Product): The product included in the item.
    """
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"total price of {self.quantity} {self.product.name}: {self.total_price()}"

    def total_price(self):
        """
        Calculate the total price of the item.

        Returns:
            Decimal: The total price of the item.
        """
        return self.quantity * self.product.price

    class Meta:
        verbose_name_plural = 'cart items'


class Coupon(BaseModel):
    """
    Model representing a coupon.

    Attributes:
        code (str): The code of the coupon.
        percent (int): The percentage discount offered by the coupon.
        deadline (datetime): The deadline for using the coupon.
        stock (int): The stock of the coupon.
        capacity_usage (int): The capacity usage of the coupon.
        is_active (bool): Indicates whether the coupon is active or not.
        user (User): The user to whom the coupon belongs.
    """
    code = models.CharField(max_length=255, unique=True)
    percent = models.PositiveIntegerField(default=1)
    deadline = models.DateTimeField()
    stock = models.PositiveIntegerField()
    capacity_usage = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.code} with {self.percent} percentage is active until {self.deadline} for {self.capacity_usage} people"

    class Meta:
        verbose_name_plural = 'coupons'


class Transaction(BaseModel):
    """
    Model representing a transaction.

    Attributes:
        final_price (Decimal): The final price of the transaction.
        transaction_type (str): The type of the transaction.
        user (User): The user involved in the transaction.
        order (Order): The order associated with the transaction.
    """
    TRANSACTION_TYPES = (
        ("accounting transactions", "accounting transactions"),
        ("receipts", "receipts"),
    )
    final_price = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=255, choices=TRANSACTION_TYPES)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"transaction: {self.final_price}"

    class Meta:
        verbose_name_plural = "transactions"

    
    