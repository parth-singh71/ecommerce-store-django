import uuid
from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    phone_number = models.CharField(null=True, blank=True, max_length=13)
    is_authorized_seller = models.BooleanField(default=False)
    cart_id = models.UUIDField(default=uuid.uuid4, auto_created=True, editable=True)


# class Cart(models.Model):
#     # id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(
#         User, on_delete=models.CASCADE, blank=True, null=True)

#     def __str__(self) -> str:
#         return f"{self.user}'s Cart"


class Product(models.Model):
    name = models.TextField(null=False, blank=False)
    description = models.TextField(default="", blank=True)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name


class Wishlist(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return self.name


class Payment(models.Model):
    PAYMENT_TYPE_CHOICES = (
        ('GPay', 'GPay'),
        ('Paytm', 'Paytm'),
        ('Amazon Pay', 'Amazon Pay'),
        ('Debit Card', 'Debit Card'),
        ('Credit Card', 'Credit Card'),
    )
    type = models.TextField(null=False, blank=False,
                            choices=PAYMENT_TYPE_CHOICES)
    amount = models.IntegerField(null=False, blank=False)
    transaction_id = models.CharField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.type} - {self.amount}"


class ProductBuyer(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    bought_at = models.DateTimeField(default=datetime.now)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.product} - {self.buyer}"


class ProductSeller(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    enlisted_at = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return f"{self.product} - {self.seller}"


class ProductCategory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    added_at = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"

    def __str__(self) -> str:
        return f"{self.product} - {self.category}"


class ProductCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    added_at = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return f"{self.product} - {self.quantity} - {self.user}'s cart"


class ProductWishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return f"{self.product} - {self.user}'s wishlist"

class UserWishlist(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    added_at = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return f"{self.user} - {self.wishlist}"
