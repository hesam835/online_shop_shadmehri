from rest_framework import serializers

from .models import Product,Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description' , 'image' , 'discount']
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name' , 'price' , 'image' , 'description' ]
        
# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ['name' , 'price' , 'image' , 'description' ]
        
        
