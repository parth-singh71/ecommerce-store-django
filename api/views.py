from rest_framework.authentication import TokenAuthentication, \
    SessionAuthentication, BasicAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import generics, mixins, viewsets
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from .models import ProductWishlist, User, Product, Payment, Category, ProductBuyer, ProductSeller, ProductCart, Wishlist, UserWishlist, ProductCategory
from .serializers import ProductWishlistExtendedSerializer, ProductWishlistSerializer, UserSerializer, ProductSerializer, PaymentSerializer, CategorySerializer, ProductBuyerSerializer, ProductSellerSerializer, ProductCartSerializer, ProductCartExtendedSerializer, WishlistSerializer, UserWishlistSerializer, ProductCategorySerializer


class UsersViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ('id', 'first_name', 'last_name',
                        'is_active', 'username', 'email')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('id')  # default


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ('id', 'name')
    search_fields = ('name', 'description')
    ordering = ('created_at')


# class CartViewset(viewsets.ModelViewSet):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer
#     filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
#     filterset_fields = ('id', 'user')
#     search_fields = ('user')
#     ordering = ('id')  # default


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ('id', 'name')
    search_fields = ('name')
    ordering = ('created_at')


class WishlistViewset(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ('id', 'name')
    search_fields = ('name')
    ordering = ('created_at')


class PaymentViewset(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ('id', 'type')
    search_fields = ('type', 'transaction_id')
    ordering = ('created_at')  # default


class ProductBuyerViewset(viewsets.ModelViewSet):
    queryset = ProductBuyer.objects.all()
    serializer_class = ProductBuyerSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ('id', 'buyer', 'product')
    search_fields = ('id', 'buyer', 'product', 'payment')
    ordering = ('bought_at')


class ProductSellerViewset(viewsets.ModelViewSet):
    queryset = ProductSeller.objects.all()
    serializer_class = ProductSellerSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ('id', 'seller')
    search_fields = ('seller')
    ordering = ('enlisted_at')


class ProductCategoryViewset(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ('id', 'product', 'category')
    search_fields = ('product', 'category')
    ordering = ('added_at')


class ProductCartViewset(viewsets.ModelViewSet):
    queryset = ProductCart.objects.all()
    serializer_class = ProductCartExtendedSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ['id', 'product', 'user']
    search_fields = ('product', 'user')
    ordering = ('added_at',)


class GenericProductCartViewset(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = ProductCartSerializer
    queryset = ProductCart.objects.all()
    lookup_field = "id"
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ['id', 'product', 'user']
    search_fields = ('product', 'user')
    ordering = ('added_at',)
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def patch(self, request, id=None):
        return self.partial_update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)



class ProductWishlistViewset(viewsets.ModelViewSet):
    queryset = ProductWishlist.objects.all()
    serializer_class = ProductWishlistExtendedSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ['id', 'product', 'user']
    search_fields = ('product', 'user')
    ordering = ('added_at',)


class GenericProductWishlistViewset(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = ProductWishlistSerializer
    queryset = ProductWishlist.objects.all()
    lookup_field = "id"
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ['id', 'product', 'user']
    search_fields = ('product', 'user')
    ordering = ('added_at',)
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def patch(self, request, id=None):
        return self.partial_update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


class UserWishlistViewset(viewsets.ModelViewSet):
    queryset = UserWishlist.objects.all()
    serializer_class = UserWishlistSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ('id', 'wishlist', 'user')
    search_fields = ('wishlist', 'user')
    ordering = ('added_at')
