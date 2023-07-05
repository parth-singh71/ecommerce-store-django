from django.urls import path, include
from rest_framework import routers
from .views import GenericProductWishlistViewset, ProductWishlistViewset, UsersViewset, ProductViewset, CategoryViewset, PaymentViewset, WishlistViewset, ProductCartViewset, GenericProductCartViewset, ProductBuyerViewset, UserWishlistViewset, ProductSellerViewset, ProductCategoryViewset


router = routers.DefaultRouter()
router.register('users', UsersViewset)
router.register('payments', PaymentViewset)
router.register('wishlists', WishlistViewset)
router.register('categories', CategoryViewset)
router.register('products', ProductViewset)
router.register('products-buyer', ProductBuyerViewset)
router.register('product-seller', ProductSellerViewset)
router.register('product-category', ProductCategoryViewset)
router.register('product-cart', ProductCartViewset)
router.register('product-wishlist', ProductWishlistViewset)
router.register('user-wishlist', UserWishlistViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('api.auth.urls')),
    path('generic/product-cart/', GenericProductCartViewset.as_view()),
    path('generic/product-wishlist/', GenericProductWishlistViewset.as_view()),
    # path('generic/record/<int:id>/', GenericRecordView.as_view()),
    # path('generic/product/', GenericProductView.as_view()),
    # path('generic/product/<int:id>/', GenericProductView.as_view()),
    # path('generic/activity/', GenericActivityView.as_view()),
    # path('generic/activity/<int:id>/', GenericActivityView.as_view()),
]
