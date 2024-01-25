from django.db import models
from accounts.models import User

# Create your models here.

class Discount_Code(models.Model):
    code = models.CharField(max_length = 10)
    percentage = models.IntegerField(max_length = 2)
    expiration_date = models.TimeField()
    is_active = models.BooleanField(default = False)
    user_id = models.ForeignKey(User,on_delete = models.CASCADE)


class Discount(models.Model):
    type = models.CharField(max_length = 50)
    price = models.DecimalField(max_digits = 10 , decimal_places = 2)
    max_value = models.DecimalField(max_digits = 10 , decimal_places = 2)
    is_active = models.BooleanField(default = False)
    user_id = models.ForeignKey(User,on_delete = models.CASCADE)
    
    
class Category(models.Model):
    name = models.CharField(max_legth = 50)
    is_sub = models.BooleanField(Default = True)
    image = models.ImageField(null = True)
    user_id = models.ForeignKey(User,on_delete = models.CASCADE)
    category_id = models.ForeignKey(on_delete = models.CASCADE)
    discount_id = models.ForeignKey(Discount,on_delete = models.CASCADE)


class Product(models.Model):

    name = models.CharField(max_length = 50)
    brand = models.CharField(max_length = 50)
    price = models.DecimalField(max_digits = 10 , decimal_places = 2)
    description = models.TextField()
    inventory_quantity = models.IntegerField(max_length = 10)
    image = models.ImageField(null = True)
    user_id = models.ForeignKey(User , on_deleted = models.CASCADE)
    category_id = models.ForeignKey(Category , on_deleted = models.CASCADE)
    discount_id = models.ForeignKey(Discount , on_deleted = models.CASCADE)
    
    