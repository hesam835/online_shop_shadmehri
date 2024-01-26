from django.db import models
from core.models import BaseModel
from accounts.models import User
from product.models import Product

# Create your models here.


class Order(BaseModel):
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    discount_code = models.ForeignKey("DiscountCode", on_delete=models.PROTECT)
    province = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    detailed_address = models.TextField()
    postal_code = models.IntegerField()
    cuppon_active = models.BooleanField(default = True)
    
    
class OrderItem(BaseModel):
    quantity = models.IntegerField()
    order = models.ForeignKey("Order", on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)



    
# Foreign keys

# user = models.ForeignKey("User", on_delete=models.PROTECT)

class Transaction(BaseModel):
    TRANSACTION_TYPES = (
    ("accounting transactions", "accounting transactions"),
    ("receipts", "receipts"),
    )

    final_price = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=255, choices=TRANSACTION_TYPES)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    order = models.OneToOneField(Order, on_delete=models.PROTECT, primary_key=True)
    # discount_code = models.ForeignKey("DiscountCode", on_delete=models.PROTECT)
    
    
    