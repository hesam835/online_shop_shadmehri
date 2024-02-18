from rest_framework import serializers
from .models import Cart , CartItem,Coupon 


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model =Cart
        fields = '__all__'
        
        
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model =CartItem
        fields = '__all__'
        
class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model =Coupon
        fields = '__all__'