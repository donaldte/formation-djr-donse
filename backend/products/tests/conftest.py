import pytest 
from django.contrib.auth.models import User
from products.models import Product
from rest_framework.test import APIClient



@pytest.fixture
def api_client() -> APIClient:
    yield APIClient()
    

@pytest.fixture
def user() -> User:
    user = User.objects.create_user(
        username='test_user', password='test_password'
    )
    return user   


@pytest.fixture
def super_user() -> User:
    user = User.objects.create_superuser(
        username='super_user', password='super_password', is_staff=True, is_active=True, is_superuser=True
    )
    return user

@pytest.fixture
def product(user) -> Product:
    product = Product.objects.create(
        name='Test Product',
        description='Test Description',
        price=100.00,
        user=user
    )
    return product 