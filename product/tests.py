from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
from rest_framework import status
from rest_framework.test import APIRequestFactory
from .models import Category, Product
from accounts.models import User
from .views import get_details, get_details_sub, ProductList, get_detail_product, get_discount, get_comment, get_productfeature, get_news, get_users

# class ProductModelTest(TestCase):

#     def setUp(self):
#         # ایجاد یک کاربر برای استفاده در تست‌ها
#         self.user = User.objects.create(
#             phone_number='09123456789',
#             email='test@example.com',
#             first_name='John',
#             last_name='Doe',
#             image='path/to/image.jpg',
#             role='Staff',
#             is_active=True
#         )

#         # ایجاد یک دسته‌بندی برای استفاده در تست‌ها
#         self.category = Category.objects.create(
#             name='Electronics',
#             is_sub=False,
#             image='path/to/category_image.jpg'
#         )

#     def test_create_product(self):
#         product = Product.objects.create(
#             name='Smartphone',
#             brand='Samsung',
#             price='500.00',
#             description='A high-quality smartphone.',
#             inventory_quantity=10,
#             image=SimpleUploadedFile("file.jpg", b"file_content", content_type="image/jpeg"),
#             user_id=self.user,
#             category_id=self.category
#         )
#         self.assertIsInstance(product, Product)
#         self.assertEqual(product.name, 'Smartphone')
#         self.assertEqual(product.brand, 'Samsung')
#         self.assertEqual(product.price, '500.00')
#         self.assertEqual(product.description, 'A high-quality smartphone.')
#         self.assertEqual(product.inventory_quantity, 10)
#         self.assertEqual(product.image.name, 'products/Electronics/file.jpg')
#         self.assertEqual(product.user_id, self.user)
#         self.assertEqual(product.category_id, self.category)

#     def test_product_str_method(self):
#         product = Product.objects.create(
#             name='Smartphone',
#             brand='Samsung',
#             price='500.00',
#             description='A high-quality smartphone.',
#             inventory_quantity=10,
#             image=SimpleUploadedFile("file.jpg", b"file_content", content_type="image/jpeg"),
#             user_id=self.user,
#             category_id=self.category
#         )
#         self.assertEqual(str(product), f'{product.name},{product.brand}')


class ViewTests(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.category = Category.objects.create(name='Test Category', slug='test-category')
        self.product = Product.objects.create(name='Test Product', slug='test-product', category=self.category)

    def test_get_details(self):
        url = reverse('get_details')
        request = self.factory.get(url)
        response = get_details(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_details_sub(self):
        url = reverse('get_details_sub', args=[self.category.slug])
        request = self.factory.get(url)
        response = get_details_sub(request, self.category.slug)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ProductList_get(self):
        url = reverse('product_list', args=[self.category.slug])
        request = self.factory.get(url)
        view = ProductList.as_view()
        response = view(request, slug=self.category.slug)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_detail_product(self):
        url = reverse('get_detail_product', args=[self.product.slug])
        request = self.factory.get(url)
        response = get_detail_product(request, self.product.slug)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_discount(self):
        url = reverse('get_discount')
        request = self.factory.get(url)
        response = get_discount(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_comment(self):
        url = reverse('get_comment', args=[self.product.slug])
        request = self.factory.get(url)
        response = get_comment(request, self.product.slug)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_productfeature(self):
        url = reverse('get_productfeature', args=[self.product.slug])
        request = self.factory.get(url)
        response = get_productfeature(request, self.product.slug)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_news(self):
        url = reverse('get_news')
        request = self.factory.get(url)
        response = get_news(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_users(self):
        url = reverse('get_users')
        request = self.factory.get(url)
        response = get_users(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
