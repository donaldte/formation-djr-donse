from products.api.filters import ProductFilter
from .serializer import ProductSerializer
from rest_framework import viewsets 
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework import mixins 
from rest_framework import permissions
from rest_framework import authentication
from .permissions import DjangoCustomModelsPermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import pagination
from django_filters import rest_framework as filters
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
# imporrt cache 
from django.core.cache import cache


class CustomPaginationClass(pagination.LimitOffsetPagination):
    default_limit = 5
    max_limit = 100


class CustomThrottleClass(UserRateThrottle, AnonRateThrottle):
    scope = 'products'
    rate = '1/min'
    rate_key = 'ip'


    

class ProductMixinApiView(
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.ListModelMixin,
        mixins.DestroyModelMixin,
        generics.GenericAPIView
    ):
    
    # caching use for queryset 
    product_cache_key = 'product_cache_key'
    if cache.get(product_cache_key):
        queryset = cache.get(product_cache_key)
    else:
        queryset = Product.objects.all()
        cache.set(product_cache_key, queryset, 380) # 60 secondes
        
    queryset = Product.objects.all()
    pagination_class = CustomPaginationClass
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter
    serializer_class = ProductSerializer
    throttle_classes = [CustomThrottleClass]
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication, JWTAuthentication]
    permission_classes = [DjangoCustomModelsPermission] #isAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated, DjangoModelPermission
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    # auth session auth token(token simple et bearer) jwt(json web token) access token et refresh token
    
    
    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            # operation = Operation()
            # operation.author = self.request.user
            # operation.entrer = 'get_queryset of ProductMixinApiView'
            # operation.sortie = 'get_queryset of ProductMixinApiView of this number of product {}'.format(self.queryset.count())
            # operation.status_code = 200
            # operation.ip_adddress = self.request.META.get('REMOTE_ADDR')
            # operation.save()
            return super().get_queryset()
        return super().get_queryset().filter(user=self.request.user)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    
    
    
       
    

class CustomProductModelViewset(ProductMixinApiView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        return super().get_queryset().filter(price__gt=100)