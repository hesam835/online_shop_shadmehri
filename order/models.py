from django.db import models
from accounts.models import User
from product.models import Discount_Code,Product

# Create your models here.


class Order(models.Model):
    total_price = models.DecimalField(max_digits = 10 , decimal_places = 2)
    is_paid = models.BooleanField(Default = False)
    user_id = models.ForeignKey(User , on_deleted = models.CASCADE)
    discount_code_id = models.ForeignKey(Discount_Code,on_deleted = models.CASCADE)
    
    
class Orde_Item(models.Model):
    quantity = models.IntegerField(max_length = 2)
    order_id = models.ForeignKey(Order , on_deleted = models.CASCADE)
    product_id = models.ForeignKey(Product , on_deleted = models.CASCADE)


class Transaction(models.Model):
    total_price = models.DecimalField(max_digits = 10 , decimal_places = 2)
    transaction_type = models.CharField(max_length = 50)
    user_id = models.ForeignKey(User , on_deleted = models.CASCADE)
    order_id = models.ForeignKey(Order , on_deleted = models.CASCADE)
    discount_code_id = models.ForeignKey(Discount_Code,on_deleted = models.CASCADE)
    
    
    