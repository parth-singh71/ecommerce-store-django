from django.db import models
from django.db.models import fields
from rest_framework import serializers, exceptions
from .models import ProductWishlist, User, Product, Payment, Category, ProductBuyer, ProductSeller, ProductCart, Wishlist, UserWishlist, ProductCategory


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        # fields = '__all__'
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'date_joined',
            'phone_number',
            'last_login',
            'cart_id',
            'is_authorized_seller',
        ]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class ProductBuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBuyer
        fields = "__all__"


class ProductSellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSeller
        fields = "__all__"


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"


class ProductCartExtendedSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = ProductCart
        fields = [
            "id",
            "user",
            "quantity",
            "added_at",
            "product"
        ]


class ProductCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCart
        fields = "__all__"


class ProductWishlistExtendedSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = ProductWishlist
        fields = [
            "id",
            "user",
            "added_at",
            "product"
        ]


class ProductWishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductWishlist
        fields = "__all__"


class UserWishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWishlist
        fields = "__all__"
