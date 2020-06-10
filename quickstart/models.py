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
    TRANSPORTER = 4

    ROLE_CHOICES = (
        (SALES_MANAGER, 'Sales Manager'),
        (SALES_MAN, 'Salesman'),
        (AGENCY, 'Agency'),
        (TRANSPORTER, 'Transporter')
    )

    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, null=True, blank=True)


class SalesManager(models.Model):
    class Meta:
        db_table = 'quickstart_sales_manager'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=32, unique=True, blank=True)
    idcard = models.CharField(max_length=128, unique=True, blank=True)
    avatar_url = models.CharField(max_length=1024, blank=True)
    phone_number = models.CharField(max_length=12, unique=True, blank=True)
    gender = models.BooleanField(default=True)
    address = models.CharField(max_length=256, blank=True)
    date_of_birth = models.DateTimeField(
        default=timezone.datetime(1996, 12, 28))
    created_at = models.DateTimeField(default=timezone.now)
    removed = models.BooleanField(default=False)

    def __str__(self):
        return self.code


class SalesMan(models.Model):
    class Meta:
        db_table = 'quickstart_salesman'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=32, unique=True, blank=True)
    idcard = models.CharField(max_length=128, unique=True, blank=True)
    avatar_url = models.CharField(max_length=1024, blank=True)
    phone_number = models.CharField(max_length=12, unique=True, blank=True)
    email = models.EmailField(max_length=128, unique=True, blank=True)
    gender = models.BooleanField(default=True)
    address = models.CharField(max_length=256, blank=True)
    date_of_birth = models.DateTimeField(
        default=timezone.datetime(1996, 12, 28))
    created_at = models.DateTimeField(default=timezone.now)
    removed = models.BooleanField(default=False)

    def __str__(self):
        return self.code


class Agency(models.Model):
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True
    )
    code = models.CharField(max_length=32, blank=True)
    name = models.CharField(max_length=128, blank=True)
    address = models.CharField(max_length=256, default='update is required')
    phone_number = models.CharField(max_length=16, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Product(models.Model):
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True,
    )
    code = models.CharField(max_length=32, unique=True, blank=True)
    name = models.CharField(max_length=256, blank=True)
    image_url = models.CharField(max_length=1024, blank=True)
    weight = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    origin = models.CharField(max_length=256, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    removed = models.BooleanField(default=False)

    def __str__(self):
        return self.code


class RequestOrder(models.Model):
    class Meta:
        db_table = 'quickstart_request_order'

    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True,
    )
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, blank=True)
    code = models.CharField(max_length=32, unique=True, blank=True)
    bill_value = models.DecimalField(
        max_digits=11, decimal_places=2, default=0)
    created_at = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)

    def __str__(self):
        return self.code


class RequestOrderDetails(models.Model):
    class Meta:
        db_table = 'quickstart_request_order_details'

    request_order = models.ForeignKey(RequestOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)


class Storage(models.Model):
    class Meta:
        db_table = 'quickstart_storage'
    code = models.CharField(max_length=32, unique=True, blank=True)
    address = models.CharField(max_length=256, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.code


class StorageProductDetails(models.Model):
    class Meta:
        db_table = 'quickstart_storage_product_details'

    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)


class DiscountStratery(models.Model):
    class Meta:
        db_table = 'quickstart_discount_stratery'

    created_at = models.DateTimeField(default=timezone.now)
