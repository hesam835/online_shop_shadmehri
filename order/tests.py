from django.test import TestCase
from django.utils import timezone
from accounts.models import User
from product.models import Product, Category, Discount
from .models import Order, OrderItem

class OrderModelTest(TestCase):

    def setUp(self):
        # ایجاد یک کاربر برای استفاده در تست‌ها
        self.user = User.objects.create(
            phone_number='09123456789',
            email='test@example.com',
            first_name='John',
            last_name='Doe',
            image='path/to/image.jpg',
            role='Customer',
            is_active=True
        )

        # ایجاد یک دسته‌بندی برای استفاده در تست‌ها
        self.category = Category.objects.create(
            name='Electronics',
            is_sub=False,
            image='path/to/category_image.jpg'
        )

        # ایجاد یک محصول برای استفاده در تست‌ها
        self.product = Product.objects.create(
            name='Smartphone',
            brand='Samsung',
            price='500.00',
            description='A high-quality smartphone.',
            inventory_quantity=10,
            image='path/to/product_image.jpg',
            user_id=self.user,
            category_id=self.category
        )

    def test_create_order(self):
        order = Order.objects.create(
            total_price=500.00,
            is_paid=True,
            province='Tehran',
            city='Tehran',
            detailed_address='123 Main St',
            postal_code='12345',
            user=self.user
        )
        self.assertIsInstance(order, Order)
        self.assertEqual(order.total_price, 500.00)
        self.assertTrue(order.is_paid)
        self.assertEqual(order.province, 'Tehran')
        self.assertEqual(order.city, 'Tehran')
        self.assertEqual(order.detailed_address, '123 Main St')
        self.assertEqual(order.postal_code, '12345')
        self.assertEqual(order.user, self.user)

    def test_create_order_item(self):
        order = Order.objects.create(
            total_price=500.00,
            is_paid=True,
            province='Tehran',
            city='Tehran',
            detailed_address='123 Main St',
            postal_code='12345',
            user=self.user
        )
        order_item = OrderItem.objects.create(
            order=order,
            product=self.product,
            quantity=2
        )
        self.assertIsInstance(order_item, OrderItem)
        self.assertEqual(order_item.order, order)
        self.assertEqual(order_item.product, self.product)
        self.assertEqual(order_item.quantity, 2)

    def test_order_str_method(self):
        order = Order.objects.create(
            total_price=500.00,
            is_paid=True,
            province='Tehran',
            city='Tehran',
            detailed_address='123 Main St',
            postal_code='12345',
            user=self.user
        )
        self.assertEqual(str(order), f"Total: {order.total_price}, Payment: {order.is_paid}")