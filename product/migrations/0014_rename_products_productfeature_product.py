# Generated by Django 5.0.1 on 2024-02-08 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_remove_product_features_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productfeature',
            old_name='products',
            new_name='product',
        ),
    ]
