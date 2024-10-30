from .serializer import ProductSerializer
from rest_framework import viewsets 
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import status

# models viewset
# mixins 
# routages 
# Relation entre les models ===> foreign key, many to many, one to one( Next )




    
    
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def product_detail_api(request, pk=None, *args, **kwargs):
    
    if request.method == 'GET':
        if pk is not None:
            product = get_object_or_404(Product, pk=pk)
            serializer = ProductSerializer(product, many=False)
            return Response(serializer.data)
        else:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        
    elif request.method == 'POST':
        data = request.data
        serializer = ProductSerializer(data=request.data)
       
       
        if serializer.is_valid(raise_exception=True):
            name = serializer.validated_data.get('name')
            description = serializer.validated_data.get('description')
            if description is None:
                description = 'No description'
            serializer.save(description=description)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)   
    
    elif request.method == 'PUT':
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors) 
    elif request.method == 'PATCH':
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'DELETE':
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response({'message': 'Product deleted successfully'})
    
    return Response({'message': 'Hello world'})    