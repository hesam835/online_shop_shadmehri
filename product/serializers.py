from rest_framework import serializers
from .models import Product, Category, Discount, ProductFeature, Comment, News, ProductFeatureValue
from accounts.models import User

class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.

    This serializer serializes Category model instances and specifies the fields to be included in the serialized data.

    Attributes:
        Meta (class): A nested class defining metadata options for the serializer.
            model (Model): The model class to be serialized.
            fields (tuple): The fields to include in the serialized data.
    """
    class Meta:
        model = Category
        fields = '__all__'
     
class DiscountSerializer(serializers.ModelSerializer):
    """
    Serializer for the Discount model.

    This serializer serializes Discount model instances and specifies the fields to be included in the serialized data.

    Attributes:
        Meta (class): A nested class defining metadata options for the serializer.
            model (Model): The model class to be serialized.
            fields (tuple): The fields to include in the serialized data.
    """
    class Meta:
        model = Discount
        fields = '__all__'
             
class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.

    This serializer serializes Product model instances and specifies the fields to be included in the serialized data.

    Attributes:
        Meta (class): A nested class defining metadata options for the serializer.
            model (Model): The model class to be serialized.
            fields (tuple): The fields to include in the serialized data.
    """
    class Meta:
        model = Product
        fields = '__all__'
        
class ProductFeatureSerializer(serializers.ModelSerializer):
    """
    Serializer for the ProductFeature model.

    This serializer serializes ProductFeature model instances and specifies the fields to be included in the serialized data.

    Attributes:
        Meta (class): A nested class defining metadata options for the serializer.
            model (Model): The model class to be serialized.
            fields (tuple): The fields to include in the serialized data.
    """
    class Meta:
        model = ProductFeature
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.

    This serializer serializes User model instances and specifies the fields to be included in the serialized data.

    Attributes:
        Meta (class): A nested class defining metadata options for the serializer.
            model (Model): The model class to be serialized.
            fields (tuple): The fields to include in the serialized data.
    """
    class Meta:
        model = User
        fields = '__all__'        

class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model.
    """
    user_id = UserSerializer()
    class Meta:
        model = Comment
        fields = '__all__'
        
class NewsSerializer(serializers.ModelSerializer):
    """
    Serializer for the News model.

    This serializer serializes News model instances and specifies the fields to be included in the serialized data.

    Attributes:
        Meta (class): A nested class defining metadata options for the serializer.
            model (Model): The model class to be serialized.
            fields (tuple): The fields to include in the serialized data.
    """
    class Meta:
        model = News
        fields = '__all__'
        
class ProductFeatureValueSerializer(serializers.ModelSerializer):
    """
    Serializer for the ProductFeatureValue model.

    This serializer serializes ProductFeatureValue model instances and specifies the fields to be included in the serialized data.

    Attributes:
        Meta (class): A nested class defining metadata options for the serializer.
            model (Model): The model class to be serialized.
            fields (tuple): The fields to include in the serialized data.
    """
    class Meta:
        model = ProductFeatureValue
        fields = '__all__'
