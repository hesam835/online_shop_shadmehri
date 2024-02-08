# Generated by Django 5.0.1 on 2024-02-08 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_productfeature_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='features',
        ),
        migrations.RemoveField(
            model_name='productfeature',
            name='numeric_value',
        ),
        migrations.RemoveField(
            model_name='productfeature',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='productfeature',
            name='text_value',
        ),
        migrations.AddField(
            model_name='productfeature',
            name='products',
            field=models.ManyToManyField(blank=True, through='product.ProductFeatureValue', to='product.product'),
        ),
        migrations.AlterField(
            model_name='productfeature',
            name='name',
            field=models.CharField(help_text='like color', max_length=255),
        ),
    ]
