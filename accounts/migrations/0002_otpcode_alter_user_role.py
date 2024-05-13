# Generated by Django 5.0.1 on 2024-02-12 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OTPCODE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=11)),
                ('code', models.PositiveSmallIntegerField()),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Product Manager', 'Product Manager'), ('Supervisor', 'Supervisor'), ('Operator', 'Operator'), ('Customer', 'Customer')], default='Customer', max_length=255),
        ),
    ]
