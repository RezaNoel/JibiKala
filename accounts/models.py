from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=11, blank=True)
    national_code = models.CharField(max_length=10, blank=True)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='user_accounts',
        related_query_name='user_account'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='user_accounts',
        related_query_name='user_account'
    )
class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.TextField()
    postal_code = models.CharField(max_length=10)
    emergency_call = models.CharField(max_length=11)
    receiver = models.CharField(max_length=60)