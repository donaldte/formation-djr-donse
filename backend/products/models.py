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
    
    
    def get_product_name(self):
        return self.name
    
    
    def get_product_description(self):
        return self.description
    
    
    def get_product_price(self):
        return self.price
    
    
    def get_product_user(self):
        return self.user.username
    
    
"""
django 2.0 l'eureur n + 1 
product = Product.objects.all().select_related('user') # jointure sql sur les foreign key et one to one
product = Product.objects.all().prefetch_related('user') # jointure sql sur les many to many 
product1 = Product.objects.filter(id=1).select_related('user').first()
product1 = get_object_or_404(Product, id=1)
iter to get each object next when is called 
product = Product.objects.all().select_related('user')
iterator = iter(product)
print(next(iterator).user.username)

for p in product:
    print(p.user.username)
"""    


class Operation(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    entrer = models.CharField(max_length=100)
    sortie = models.CharField(max_length=100)
    status_code = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    ip_adddress = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.entrer