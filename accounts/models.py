from django.db import models

# Create your models here.

class User(models.Model):
    STAFF_CHOICES = [
    ('Customer','Customer'),
    ('Admin','Admin'),
    ('Supervisor','Supervisor')
    ]

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    image = models.ImageField(null=True)
    role = models.CharField(max_length = 30 , choices=STAFF_CHOICES)

class adress(models.Model):
    province = models.CharField(max_length=3)
    city = models.CharField(max_length = 50)
    detailed_address = models.TextField()
    postal_code = models.BigIntegerField()


