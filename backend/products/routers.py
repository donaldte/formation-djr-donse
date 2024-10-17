from .api import api 
from .api import api_viewset
from rest_framework.routers import DefaultRouter, SimpleRouter

# defaultrouter et le simplerouter

router = DefaultRouter()
router.register(r'products', api_viewset.ProductViewSet, basename='products')
router.register(r'users', api_viewset.UserViewSet)
"""
DefaultRouter est un routeur qui génère automatiquement les URL pour les vues de l'ensemble
de vues.
SimpleRouter est un routeur qui génère automatiquement les URL pour les vues 
de l'ensemble de vues, mais ne génère pas de routes pour les actions de création et 
de suppression.
"""

urlpatterns = router.urls