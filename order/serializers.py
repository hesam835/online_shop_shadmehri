from rest_framework import serializers
from .models import Cart, CartItem, Coupon, Order, OrderItem
from accounts.models import Address, User
from product.models import Product
from product.serializers import UserSerializer

class CartSerializer(serializers.ModelSerializer):
    """
    Serializer for the Cart model.

    This serializer serializes Cart model instances and specifies the fields to be included in the serialized data.

    Attributes:
        Meta (class): A nested class defining metadata options for the serializer.
            model (Model): The model class to be serialized.
            fields (tuple): The fields to include in the serialized data.
    """
    class Meta:
        model = Cart
        fields = '__all__'

class CartItemSerializer(serializers.Serializer):
    """
    Serializer for CartItem instances.

    This serializer validates and serializes CartItem instances and ensures the correctness of the data.

    Attributes:
        product_id (IntegerField): The ID of the product associated with the cart item.
        quantity (IntegerField): The quantity of the product in the cart item.

    Methods:
        validate_product_id(value): Validates the product ID to ensure it exists in the database.
        validate(data): Validates the product ID and quantity to ensure they meet the specified criteria.
    """
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()

    def validate_product_id(self, value):
        """
        Validates the product ID to ensure it exists in the database.

        Args:
            value (int): The product ID.

        Returns:
            int: The validated product ID.

        Raises:
            serializers.ValidationError: If the product with the provided ID does not exist.
        """
        try:
            product = Product.objects.get(pk=value)
        except Product.DoesNotExist:
            raise serializers.ValidationError("Product with id '{}' does not exist.".format(value))
        return product

    def validate(self, data):
        """
        Validates the product ID and quantity to ensure they meet the specified criteria.

        Args:
            data (dict): The data containing product ID and quantity.

        Returns:
            dict: The validated data.

        Raises:
            serializers.ValidationError: If the quantity is less than or equal to zero or if the product with the provided ID does not exist.
        """
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
    """
    Serializer for the Coupon model.

    This serializer serializes Coupon model instances and specifies the fields to be included in the serialized data.

    Attributes:
        Meta (class): A nested class defining metadata options for the serializer.
            model (Model): The model class to be serialized.
            fields (tuple): The fields to include in the serialized data.
    """
    class Meta:
        model = Coupon
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for the Order model.

    This serializer serializes Order model instances and specifies the fields to be included in the serialized data.
    It also includes the user information using the UserSerializer.

    Attributes:
        user (UserSerializer): Serializer for the user associated with the order.

    Methods:
        create(validated_data): Overrides the default create method to include the current user.
    """
    user = UserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        """
        Creates a new Order instance with the current user.

        Args:
            validated_data (dict): The validated data for creating the order.

        Returns:
            Order: The newly created order instance.
        """
        user = self.context['request'].user
        # Perform order creation logic here
        # Return the created order instance

class OrderItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the OrderItem model.

    This serializer serializes OrderItem model instances and specifies the fields to be included in the serialized data.

    Attributes:
        Meta (class): A nested class defining metadata options for the serializer.
            model (Model): The model class to be serialized.
            fields (tuple): The fields to include in the serialized data.
    """
    class Meta:
        model = OrderItem
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    """
    Serializer for the Address model.

    This serializer serializes Address model instances and specifies the fields to be included in the serialized data.
    It also includes the user information using the UserSerializer.

    Attributes:
        user (UserSerializer): Serializer for the user associated with the address.

    Attributes:
        Meta (class): A nested class defining metadata options for the serializer.
            model (Model): The model class to be serialized.
            fields (tuple): The fields to include in the serialized data.
    """
    user = UserSerializer()

    class Meta:
        model = Address
        fields = '__all__'

class AddressSaveSerializer(serializers.ModelSerializer):
    """
    Serializer for saving Address instances.

    This serializer is used when saving Address instances and includes the user information.

    Attributes:
        user (UserSerializer): Serializer for the user associated with the address.

    Attributes:
        Meta (class): A nested class defining metadata options for the serializer.
            model (Model): The model class to be serialized.
            fields (tuple): The fields to include in the serialized data.
    """
    user = UserSerializer()

    class Meta:
        model = Address
        fields = '__all__'

