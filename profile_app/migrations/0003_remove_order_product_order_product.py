# Generated by Django 5.0.4 on 2024-05-26 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_productimage'),
        ('profile_app', '0002_order_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(to='products.product'),
        ),
    ]
