from rest_framework import permissions
from django.contrib.auth.models import Permission, Group, User



class DjangoCustomModelsPermission(permissions.DjangoModelPermissions):
    
    def has_object_permission(self, request, view, obj):
        user = request.user
        # if user.is_superuser:
        #     return True
        # if user.is_staff:
        #     return True
        
        if user.is_authenticated:
            if request.method in permissions.SAFE_METHODS:
                return True
            if request.method in ['PUT', 'PATCH', 'DELETE']:
                return obj.user == user
            
        # if view.action in ['retrieve', 'list']:
        #     return True    
        
        # if view.action in ['create', 'update', 'partial_update', 'destroy']:
        #     return False
        
        return super().has_object_permission(request, view, obj)
    
    
    def has_permission(self, request, view):
        # is est que l'utiilisateur connected a la permission de add ou change ou delete
    
        
        if request.user.is_staff:
            if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
                user = request.user
                if user.has_perms('products.add_product', 'products.change_product', 'products.delete_product'):
                    return True
        
        if request.user.is_authenticated:
            if request.method in permissions.SAFE_METHODS:
                return True
            
        if request.method in ['POST']:
            if request.user.is_authenticated:
                user = request.user
                if user.has_perm('products.add_product'):
                    return True
                
                
                
        return super().has_permission(request, view)