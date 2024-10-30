import pytest 
from products.models import Product


@pytest.mark.django_db
def test_product_name(product: Product):
    assert product.get_product_name() == product.name
    
    
@pytest.mark.django_db
def test_product_description(product: Product):
    assert product.get_product_description() == product.description
    
    
@pytest.mark.django_db
def test_product_price(product: Product):
    assert product.get_product_price() == product.price
    
        