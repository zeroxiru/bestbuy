import products as products

#from products import Product

class Store:
    """
            Represents the store class that contains a list of products.
     """
    def __init__(self, products =[]):

        """
        Initializes a store instances with a list of products.

        Args:
            products (list, optional): List of Product instances. Defaults to an empty list.
        """
        self._products = products

    def add_product(self, new_product):
        """
        Adds a product to the store.

        Args:
           A product instances will be added into the list of store.
        """
        if new_product in self._products:
            self._products.append(new_product)
        else:
            raise ValueError("Product not found in the store.")

    def remove_product(self, rem_product):
        """
        Removes a product to the store.

        Args:
           A product instances will be removed from the list of store.

        """
        if rem_product in self._products:
            self._products.remove(rem_product)
        else:
            raise ValueError("Product not found in the store.")

    def get_total_quantity(self) -> int:
        """
        Get the total quantity of the product from the store list
        Args:

        Returns:
            It returns how many items it the store in total.

        """
        total_quantity = sum(product._quantity for product in self._products)
        return total_quantity

    def get_all_products(self) -> list[products.Product]:
        """
         Returns a list of all active products in the store.

        Returns:
            List[Product]: List of active Product instance[]s.
        """
        # active_product = []
        # for item_product in self.products:
        #     if item_product.is_active():
        #         active_product.append(item_product)
        # return active_product
        active_products = [product for product in self._products if product.is_active()]

        return active_products




    def  order(self, shopping_list) -> float:
        """
        Buys the products from the shopping list and returns the total price of the order.

        Args:
            shopping_list (list): List of tuples, where each tuple contains a Product and a quantity.

        Returns:
            float: Total price of the order.
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            if product in self._products and product.is_active():
                if product._quantity >= quantity:
                    total_price += product.buy(quantity)
                else:
                    raise ValueError(f"Insufficient quantity for {product._name}")
                    product.deactivate()
            else:
                raise ValueError(f"Product {product._name} is not available or not active")
        return total_price



