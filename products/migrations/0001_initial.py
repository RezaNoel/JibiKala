# Generated by Django 5.0.4 on 2024-05-06 21:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='productBrands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('faname', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='productColors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('faname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='productOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='productStorages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=128)),
            ],
        ),
        migrations.CreateModel(
            name='phoneProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('S', 'Smart Phone'), ('T', 'Tablet'), ('L', 'Laptop'), ('P', 'PC')], max_length=5)),
                ('phone_model', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.TextField(blank=True)),
                ('part', models.CharField(blank=True, choices=[('M', 'Monitor'), ('K', 'Keyboard'), ('MS', 'Mouse')], max_length=5)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productbrands')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productcolors')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productstorages')),
            ],
        ),
        migrations.CreateModel(
            name='productAttributs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=250)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.phoneproducts')),
                ('options', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productoptions')),
            ],
        ),
    ]
