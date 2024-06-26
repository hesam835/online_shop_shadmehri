# Generated by Django 5.0.1 on 2024-02-09 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_rename_product_productfeature_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productfeature',
            name='products',
        ),
        migrations.AddField(
            model_name='product',
            name='features',
            field=models.ManyToManyField(blank=True, through='product.ProductFeatureValue', to='product.productfeature'),
        ),
    ]
