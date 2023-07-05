from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Payment, Product, Category, Wishlist, ProductBuyer, ProductSeller, ProductCart, ProductCategory, UserWishlist, ProductWishlist

# Register your models here.


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name',
                    'phone_number', 'is_staff', 'is_active', 'is_authorized_seller')
    list_filter = ('is_active', 'is_staff')
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            # group heading of your choice; set to None for a blank space instead of a header
            'User Details',
            {
                'fields': (
                    'phone_number', 'is_authorized_seller', 'cart_id'
                ),
            },
        ),
    )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''Admin View for Product'''

    list_display = ('name', 'price', 'quantity')
    list_filter = ('quantity',)
    search_fields = ('name', 'description')
    date_hierarchy = 'created_at'


# @admin.register(Cart)
# class CartAdmin(admin.ModelAdmin):
#     '''Admin View for Cart'''

#     list_display = ('id', 'user',)
#     list_filter = ('user',)
#     search_fields = ('user',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Category'''

    list_display = ('name',)
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    '''Admin View for Wishlist'''

    list_display = ('name',)
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    '''Admin View for Payment'''

    list_display = ('type', 'amount', 'transaction_id', 'user', 'created_at',)
    list_filter = ('type', 'user',)
    search_fields = ('transaction_id', 'user',)
    date_hierarchy = 'created_at'


@admin.register(ProductBuyer)
class ProductBuyerAdmin(admin.ModelAdmin):
    '''Admin View for ProductBuyer'''

    list_display = ('product', 'buyer', 'quantity', 'payment',)
    list_filter = ('buyer', 'product',)
    search_fields = ('buyer', 'product',)
    date_hierarchy = 'bought_at'


@admin.register(ProductSeller)
class ProductSellerAdmin(admin.ModelAdmin):
    '''Admin View for ProductSeller'''

    list_display = ('product', 'seller', 'quantity',)
    list_filter = ('seller', 'product',)
    search_fields = ('seller', 'product',)
    date_hierarchy = 'enlisted_at'


@admin.register(ProductCart)
class ProductCartAdmin(admin.ModelAdmin):
    '''Admin View for ProductCart'''

    list_display = ('user', 'product',)
    list_filter = ('user', 'product',)
    date_hierarchy = 'added_at'


@admin.register(ProductWishlist)
class ProductWishlistAdmin(admin.ModelAdmin):
    '''Admin View for ProductWishlist'''

    list_display = ('user', 'product',)
    list_filter = ('user', 'product',)
    date_hierarchy = 'added_at'


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    '''Admin View for ProductCategory'''

    list_display = ('product', 'category')
    list_filter = ('category', 'product',)
    date_hierarchy = 'added_at'


@admin.register(UserWishlist)
class UserWishlistAdmin(admin.ModelAdmin):
    '''Admin View for UserWishlist'''

    list_display = ('wishlist', 'user',)
    list_filter = ('wishlist', 'user',)
    date_hierarchy = 'added_at'


admin.site.register(User, CustomUserAdmin)
