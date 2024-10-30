import pytest 
import logging 
from django.urls import reverse 



logger = logging.getLogger(__name__)


@pytest.mark.django_db
def test_product_create_api(api_client, user):
    url = reverse('api_2')
    response = api_client.post(url, {
        'name': 'Test Product',
        'description': 'Test Description',
        'price': 100.00,
        'user': user,
        'email': 'test@gmail.com',
    })
    assert response.status_code == 201
    assert response.data['name'] == 'Test Product'
    assert response.data['description'] == 'Test Description'
    assert response.data['price'] == '100.00'
    assert response.data['username'] == user.username
    
    
@pytest.mark.django_db
def test_product_create_api_with_authentication(api_client, super_user):
    user = super_user
    url = reverse('api_3')
    api_client.force_authenticate(user=user)
    response = api_client.post(url, {
        'name': 'Test Product',
        'description': 'Test Description',
        'price': 100.00,
        'email': 'test@gmail.com',
    })
    
    assert response.status_code == 201
    assert response.data['name'] == 'Test Product'
    assert response.data['description'] == 'Test Description'
    assert response.data['price'] == '100.00'
    assert response.data['username'] == user.username
    logger.info(response.data)