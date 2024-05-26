# Generated by Django 5.0.4 on 2024-05-24 12:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_cartitem_price'),
        ('products', '0006_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='color',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.productcolor'),
            preserve_default=False,
        ),
    ]