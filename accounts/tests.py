from django.test import TestCase
from django.utils import timezone
from .models import User

class UserModelTest(TestCase):

    def create_user(self, phone_number='12345678901', email='test@example.com',
                    first_name='John', last_name='Doe', password='testpassword',
                    address='123 Main St'):
        return User.objects.create(phone_number=phone_number, email=email,
                                   first_name=first_name, last_name=last_name,
                                   password=password, address=address)

    def test_user_creation(self):
        user = self.create_user()
        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.__str__(), user.phone_number)

    def test_convert_to_english_numbers(self):
        user = self.create_user(phone_number='۰۹۱۲۳۴۵۶۷۸۹')
        self.assertEqual(user.convert_to_english_numbers(user.phone_number), '09123456789')

    def test_clean_phone(self):
        cleaned_phone = User().clean_phone('۰۹۱۲۳۴۵۶۷۸۹')
        self.assertEqual(cleaned_phone, '09123456789')

    def test_delete_user(self):
        user = self.create_user()
        user.delete()
        self.assertTrue(user.is_deleted)

    def test_user_str_method(self):
        user = self.create_user()
        self.assertEqual(str(user), user.phone_number)

    def test_has_perm_method(self):
        user = self.create_user()
        self.assertTrue(user.has_perm('some_permission'))

    def test_has_module_perms_method(self):
        user = self.create_user()
        self.assertTrue(user.has_module_perms('some_module'))
