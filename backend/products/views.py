import json
from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import Product

def api_view(request):
    product = Product.objects.all().order_by('?').first()
    data = {}
    if product:
        data = model_to_dict(product, fields=['name', 'price'])
   
    return JsonResponse(data)