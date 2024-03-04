from rest_framework import serializers
from .models import Cart , CartItem,Coupon ,Order,OrderItem
from accounts.models import Address,User
from product.models import Product
from product.serializers import UserSerializer
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model =Cart
        fields = '__all__'
        

class CartItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()

    def validate_product_id(self, value):
        try:
            product = Product.objects.get(pk=value)
        except Product.DoesNotExist:
            raise serializers.ValidationError("Product with id '{}' does not exist.".format(value))
        return product

    def validate(self, data):
        if 'product_id' in data and 'quantity' in data:
            product_id = data['product_id']
            quantity = data['quantity']
            if quantity <= 0:
                raise serializers.ValidationError("Quantity must be greater than zero.")
            if product_id:
                try:
                    product = Product.objects.get(pk=product_id)
                except Product.DoesNotExist:
                    raise serializers.ValidationError("Product with id '{}' does not exist.".format(product_id))
        return data
        
class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model =Coupon
        fields = '__all__'
        

class OrderSerializer(serializers.ModelSerializer):

    user=UserSerializer(read_only=True)
    class Meta:
        model=Order
        fields='__all__'
        
    def create(self, validated_data):
        user = self.context['request'].user
        
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields='__all__'
        
class AddressSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model = Address
        fields = '__all__'
        
class AddressSaveSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Address
        fields = '__all__'


