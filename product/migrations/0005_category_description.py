# Generated by Django 5.0.1 on 2024-02-05 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_comment_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(default='its nice'),
            preserve_default=False,
        ),
    ]
