# from django.test import TestCase
# from django.utils import timezone
# from .models import BaseModel

# class BaseModelTestCase(TestCase):

#     def test_soft_delete(self):
#         # Create a BaseModel instance
#         base_model = BaseModel.objects.create()

#         # Check that the created_at and updated_at fields are set
#         self.assertIsNotNone(base_model.created_at)
#         self.assertIsNotNone(base_model.updated_at)

#         # Check that is_deleted and deleted_at fields are set to default values
#         self.assertFalse(base_model.is_deleted)
#         self.assertIsNone(base_model.deleted_at)

#         # Soft delete the instance
#         base_model.delete()

#         # Check that is_deleted is set to True and deleted_at is updated
#         self.assertTrue(base_model.is_deleted)
#         self.assertIsNotNone(base_model.deleted_at)

#         # Query the database to ensure the soft-deleted instance is excluded by default
#         self.assertEqual(BaseModel.objects.count(), 0)

#         # Query the soft-deleted instance explicitly
#         soft_deleted_instance = BaseModel.objects.filter(is_deleted=True).first()
#         self.assertIsNotNone(soft_deleted_instance)
#         self.assertEqual(soft_deleted_instance, base_model)

#         # Restore the soft-deleted instance
#         soft_deleted_instance.delete(soft_delete=False)

#         # Check that is_deleted is set to False
#         self.assertFalse(soft_deleted_instance.is_deleted)

#         # Query the database to ensure the instance is included again
#         self.assertEqual(BaseModel.objects.count(), 1)
