# Generated by Django 5.0.4 on 2024-05-22 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='price',
            field=models.IntegerField(),
        ),
    ]
