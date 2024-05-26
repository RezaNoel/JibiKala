# Generated by Django 5.0.4 on 2024-05-25 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_user_fisrt_name_alter_user_first_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('postal_code', models.CharField(max_length=10)),
                ('emergency_call', models.CharField(max_length=11)),
                ('receiver', models.CharField(max_length=60)),
            ],
        ),
    ]