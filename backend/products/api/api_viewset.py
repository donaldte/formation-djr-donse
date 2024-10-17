from .serializer import ProductSerializer, UserSerializer
from rest_framework import viewsets 
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.decorators import action
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductViewSet(viewsets.ModelViewSet): 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post', 'put', 'patch']
    # action to get product with highest price 
    @action(detail=False, methods=['GET'], url_path='highest-price', url_name='highest-price')
    def highest_price(self, request, *args, **kwargs):
        product = Product.objects.order_by('-price').first()
        serializer = self.get_serializer(product)
        return Response(serializer.data)
    
    
class ProductViewSetReadOnly(viewsets.ReadOnlyModelViewSet): 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
  
 
    
