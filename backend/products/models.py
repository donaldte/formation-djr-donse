from django.db import models
from django.contrib.auth.models import User
class Product(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
    def get_amount(self):
        return f'{self.price} FCFA'
    
    
    def get_discount_price(self):
        return self.price - 1000