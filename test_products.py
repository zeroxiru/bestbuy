import pytest
from products import Product

def test_creating_product():
    # Test data
    prod_name = "Apple IPhone 15 pro"
    prod_price = 1200.00
    prod_quantity = 100

    # Create a Product instance
    product = Product(prod_name, prod_price, prod_quantity)

    # Assertions to check if the product attributes are set correctly
    assert product._name == prod_name
    assert product._price == prod_price
    assert product._quantity == prod_quantity
    assert product.is_active()


def test_creating_prod_invalid_details():

    # Test creating a product with an empty name
    try:
        Product("", -120.22, 200)
        assert False, "Expected value error for empty name"
    except ValueError as e:
        assert "Name cannot be empty" in str(e)
    try:
        Product("Apple", -20.22, 200)
        assert False, "Expected value error for negative price"
    except ValueError as e:
        assert "Price cannot be negative" in str(e)
    try:
        Product("apple", 120.22, -200)
        assert False, "Expected value error for negative quantity"
    except ValueError as e:
        assert "Quantity cannot be negative" in str(e)


def test_product_with_inactive():
    product = Product("Apple watch", 123.50, 1)

    # Ensure that product is  active initially
    assert product.is_active()

    # Buy all available quantities, which should set quantity to 0
    product.buy(1)

    # check the prodict is set to inactive now
    assert not product.is_active()

def test_purchase_modify_quantity():
    product = Product("Samsung", 1500.50, 100)

    total_price = product.buy(50)

    assert product.get_quantity() == 50
    assert total_price == 1500.50 * 50


def test_buying_larger_quantity():
    product = Product("Samsung", 1500.50, 100)

    with pytest.raises(ValueError) as error:
        product.buy(120)

    # Check if the error message indicates that the provided amount is not available
    assert  "The provided amount is not available" in str(error.value)

    # check that the products quantity remains unchanged
    assert  product.get_quantity() == 100





