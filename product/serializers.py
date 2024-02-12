from rest_framework import serializers

from .models import Product,Category,Discount,ProductFeature,Comment,News,ProductFeatureValue
from accounts.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields ='__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields ='__all__'
        
        
class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields ='__all__'
        
class ProductFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeature
        fields ='__all__'

        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields ='__all__'
        
        
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields ='__all__'
        
class ProductFeatureValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeatureValue
        fields ='__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields ='__all__'        
