# Generated by Django 5.0.1 on 2024-02-05 06:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='order.cart'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_paid',
            field=models.CharField(choices=[('Paid', True), ('Not Paid', False)], default=False, max_length=25),
        ),
    ]
