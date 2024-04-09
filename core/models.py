from django.db import models
from django.db.models import Manager, QuerySet

class AppQuerySet(QuerySet):
    """
    Custom queryset for the application models.

    This queryset sets the default behavior for database queries, including filtering and deleting.
    """
    def delete(self):
        """
        Soft delete queryset items.

        Sets the 'is_deleted' attribute to True for all items in the queryset.
        """
        self.update(is_deleted=True)

class AppManager(Manager):
    """
    Custom manager for the application models.

    This manager defines the default queryset for the models, excluding deleted items.
    """
    def get_queryset(self):
        """
        Get the queryset for the model.

        Returns:
            QuerySet: The queryset for the model, excluding deleted items.
        """
        return QuerySet(self.model, using=self._db).exclude(is_deleted=True)

class BaseModel(models.Model):
    """
    Abstract base model for all application models.

    This model provides common fields and functionality for all models in the application.
    """
    class Meta:
        abstract = True
   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(auto_now=True, editable=False)
        
    def delete(self):
        """
        Soft delete the model instance.

        Sets the 'is_deleted' attribute to True and saves the instance.
        """
        self.is_deleted = True
        self.save()
    objects = AppManager()
