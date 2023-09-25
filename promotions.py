import abc


class Promotion(abc.ABC):
    """
    This class outlines a common interface for promotions. Subclasses are required to implement
    the abstract method get_promotion_discount(), which computes the
    final price after applying the discount.

Attributes:
- _name (str): The name of the promotion
    """
    def __init__(self, name):
        self._name = name

    def get_name(self) -> str:

        return self._name

    def set_name(self, value):
        self._name = value

    def apply_promotion(self, price: float, quantity: int) -> float:
        """

        Calculate the total price after applying the promotional discount.

        Parameters:
            - quantity (int): The quantity of items being purchased.
            - price (float): The original price of each item.

        Returns:
            float: The updated total price after applying the discount.
        """
        pass


class PercentagePromotion(Promotion):
    def __init__(self, name, percentage):
        super().__init__(name)
        self._percentage = percentage

    def apply_promotion(self, price: float, quantity: int) -> float:
        total_price = price * quantity
        total_amount_after_discount = total_price * ((100 - self._percentage) / 100)
        return round(total_amount_after_discount, 2)


class SecondProductHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, price: float, quantity: int) -> float:
        """
        Apply the "Second item at half price" promotion to a product.

        Args:
            price (float): The original price of the product.
            quantity (int): The quantity of items to apply the promotion to.

        Returns:
            float: The discounted price after applying the promotion.

        Example:
            In second product half price promotion, it will get 50% off at every second item of
            the given quantity like if a product price is 10 then second price will 5 of the product and
            total price  will be 15.

        Note:
            If the quantity is less than 2, no promotion is applied, and the original price is returned.
        """
        if quantity >= 2:
            discount_amount = .50
            total_quantity_of_products = (quantity + 1) // 2
            discount_number_of_products = quantity - total_quantity_of_products
            total_price = (total_quantity_of_products * price) + (discount_number_of_products * price * discount_amount)
            return total_price
        else:
            price * quantity



class BuyTwoGetOneFree(Promotion):

    def __init__(self, name):
        super().__init__(name)
    def apply_promotion(self, quantity, price) -> float:
        """
        Calculate the total discount for a "Buy 2, get 1 free" promotion.

        Args:
            quantity (int): The quantity of items for which the promotion discount is calculated.
            price (float): The original price of each item.

        Returns:
            float: The total discount after applying the promotion.

        Raises:
            ValueError: If the quantity or price is invalid (negative or zero).

        Example:
            For quantity=7 and price=10, this function calculates a total discount of $50.
        """
        try:
            if quantity <= 0 or price <= 0:
                raise ValueError("Quantity and price must be positive values.")

            # Calculate the number of free products
            free_products = (quantity // 3)

            # Calculate the total discount by summing both discounts
            total_price = (quantity - free_products) * price

            return round(total_price, 2)
        except ValueError as ve:
            raise ve


