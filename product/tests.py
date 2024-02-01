from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from accounts.models import User
from product.models import Product, Category, Discount

class ProductModelTest(TestCase):

    def setUp(self):
        # ایجاد یک کاربر برای استفاده در تست‌ها
        self.user = User.objects.create(
            phone_number='09123456789',
            email='test@example.com',
            first_name='John',
            last_name='Doe',
            image='path/to/image.jpg',
            role='Staff',
            is_active=True
        )

        # ایجاد یک دسته‌بندی برای استفاده در تست‌ها
        self.category = Category.objects.create(
            name='Electronics',
            is_sub=False,
            image='path/to/category_image.jpg'
        )

    def test_create_product(self):
        product = Product.objects.create(
            name='Smartphone',
            brand='Samsung',
            price='500.00',
            description='A high-quality smartphone.',
            inventory_quantity=10,
            image=SimpleUploadedFile("file.jpg", b"file_content", content_type="image/jpeg"),
            user_id=self.user,
            category_id=self.category
        )
        self.assertIsInstance(product, Product)
        self.assertEqual(product.name, 'Smartphone')
        self.assertEqual(product.brand, 'Samsung')
        self.assertEqual(product.price, '500.00')
        self.assertEqual(product.description, 'A high-quality smartphone.')
        self.assertEqual(product.inventory_quantity, 10)
        self.assertEqual(product.image.name, 'products/Electronics/file.jpg')
        self.assertEqual(product.user_id, self.user)
        self.assertEqual(product.category_id, self.category)

    def test_product_str_method(self):
        product = Product.objects.create(
            name='Smartphone',
            brand='Samsung',
            price='500.00',
            description='A high-quality smartphone.',
            inventory_quantity=10,
            image=SimpleUploadedFile("file.jpg", b"file_content", content_type="image/jpeg"),
            user_id=self.user,
            category_id=self.category
        )
        self.assertEqual(str(product), f'{product.name},{product.brand}')