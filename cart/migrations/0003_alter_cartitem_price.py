# Generated by Django 5.0.4 on 2024-05-22 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_cartitem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]