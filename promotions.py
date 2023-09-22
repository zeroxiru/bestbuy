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

    def apply_promotion(self, product: int, quantity: float) -> float:
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
    def __init__(self,):

class SecondProductHalfPrice(Promotion):
    pass


class BuyTwoGetOneFree(Promotion):

