from django.urls import path
from .views import api_view
from .api.api import product_detail_api
from .api.api_mixins import CustomProductModelViewset, ProductMixinApiView
from rest_framework.authtoken.views import obtain_auth_token
 
urlpatterns = [
    #path('api/', api_view, name='api')
    path('api/crud/<int:pk>/', product_detail_api, name='api_1'),
    path('api/crud/', product_detail_api, name='api_2'),
    path('api/mixins/', ProductMixinApiView.as_view(), name='api_3'),
    path('api/mixins/<int:pk>/', ProductMixinApiView.as_view(), name='api-detail'),
    path('api/login/', obtain_auth_token, name='api_login'),
]