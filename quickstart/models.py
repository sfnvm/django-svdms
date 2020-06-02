from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser
from django.dispatch import receiver


class User(AbstractUser):
    SALES_MANAGER = 1
    SALES_MAN = 2
    AGENCY = 3

    ROLE_CHOICES = (
        (SALES_MANAGER, 'Sales Manager'),
        (SALES_MAN, 'Salesman'),
        (AGENCY, 'Agency')
    )
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, blank=True, blank=True)


class SalesManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=128, unique=True, blank=True)
    idcard = models.CharField(max_length=128, unique=True, blank=True)
    phone_number = models.CharField(max_length=12, unique=True, blank=True)
    email = models.EmailField(max_length=128, unique=True, blank=True)
    address = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField(default=timezone.datetime(1996, 12, 28))
    date_created = models.DateField(default=timezone.now)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.code


class SalesMan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=128, unique=True, blank=True)
    idcard = models.CharField(max_length=128, unique=True, blank=True)
    phone_number = models.CharField(max_length=12, unique=True, blank=True)
    email = models.EmailField(max_length=128, unique=True, blank=True)
    address = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField(default=timezone.datetime(1996, 12, 28))
    date_created = models.DateField(default=timezone.now)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.code


class Agency(models.Model):
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=CASCADE, blank=True
    )
    created_date = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=128, blank=True)
    address = models.CharField(max_length=255, default='update is required')

    def __str__(self):
        return self.name


class Product(models.Model):
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=CASCADE, blank=True
    )
    created_date = models.DateTimeField(default=timezone.now)


# class Author(models.Model):
#     name = models.CharField(max_length=200)
#     added_by = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
#     created_date = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.name


# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.CharField(max_length=300)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     added_by = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
#     created_date = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.title
