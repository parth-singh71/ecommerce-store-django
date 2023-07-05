from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, Product, ProductBuyer, ProductSeller


# @receiver(post_save, sender=User)
# def create_user_cart(sender, instance, created, **kwargs):
#     if created:
#         Cart.objects.create(user=instance)


@receiver(post_save, sender=ProductBuyer)
def decrease_product_quantity(sender, instance, created, **kwargs):
    if created:
        product = Product.objects.get(id=instance.product.id)
        product.quantity -= instance.quantity
        if product.quantity < 0: 
            product.quantity = 0
        product.save()


@receiver(post_save, sender=ProductSeller)
def increase_product_quantity(sender, instance, created, **kwargs):
    if created:
        product = Product.objects.get(id=instance.product.id)
        if product.quantity < 0: 
            product.quantity = 0
        product.quantity += instance.quantity
        product.save()



@receiver(pre_save, sender=ProductBuyer)
def create_user_cart(sender, instance, **kwargs):
    product = Product.objects.get(id=instance.product.id)
    if product.quantity < instance.product.id:
        raise Exception("Not enough quantity left in inventory")

