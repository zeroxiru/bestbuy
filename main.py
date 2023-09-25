
import store
import products
import promotions


def start(store_obj):
    """
    Display the store menu and handle user interactions.

    Args:
        store_obj (Store): An instance of the Store class representing the store inventory.
    """
    try:
        promotion_totals = {}  # Dictionary to store promotion totals
        without_promotion_total = 0.0
        total_price = 0.0  # Total order price

        while True:
            print("Store Menu\n----------")
            print("1. List all products in store")
            print("2. Show total quantity in store")
            print("3. Make an order")
            print("4. Quit")

            choice = input("Please choose a number: ")

            if choice == "1":
                all_products = store_obj.get_all_products()
                for idx, product in enumerate(all_products, start=1):
                    print(f"{idx}. {product.show()}")
            elif choice == "2":
                total_quantity = store_obj.get_total_quantity()
                print(f'Total quantity in store: {total_quantity}')
            elif choice == '3':
                print("------")
                products = store_obj.get_all_products()
                for idx, product in enumerate(products, start=1):
                    print(f'{idx}. {product.show()}')
                print("------")

                order_list = []
                new_promotion = None  # Initialize the None for new promotion.

                while True:
                    product_num = input("Which product # do you want? ")
                    if not product_num:
                        break

                    product_num = int(product_num) - 1  # Adjust for 0-based indexing
                    selected_product = products[product_num]  # Access the selected product directly
                    amount = int(input("What amount do you want? "))

                    # Determine promotion switch message based on the selected product's promotion
                    promotion = selected_product.get_promotion()

                    total_price = selected_product.buy(amount)

                    if promotion:
                        promotion_name = promotion.get_name()
                        if isinstance(promotion, promotions.SecondProductHalfPrice):
                            promotion_amount = "Second item fifty percent off"
                        elif isinstance(promotion, promotions.BuyTwoGetOneFree):
                            promotion_amount = "Third item is Free"
                        elif isinstance(promotion, promotions.PercentagePromotion):
                            promotion_amount = f"{promotion._percentage} percent discount"
                        else:
                            promotion_amount = promotion.get_amount()
                    else:
                        promotion_name = "Without Promotion"
                        promotion_amount = ""

                    if promotion_name != "Without Promotion":
                        if promotion_name in promotion_totals:
                            promotion_totals[promotion_name] += total_price
                        else:
                            promotion_totals[promotion_name] = total_price
                    else:
                        without_promotion_total += total_price

                    if promotion != new_promotion:
                        if new_promotion is not None:
                            print(f"Switching to new promotion: {promotion_name} ({promotion_amount} )")
                            continue_or_exit = input("New promotion detected. Continue with new promotion (Y/N)? ").strip()
                            if continue_or_exit.lower() != 'y':
                                break

                    order_list.append((selected_product, amount))
                    #total_price += selected_product.buy(amount)
                    new_promotion = selected_product.get_promotion()

                    # Print promotion details every time
                    print("********")
                    print(f"Order made! Total payment: ${total_price:.2f}")
                    if promotion_name != "Without Promotion":
                        print(f"Promotion: {promotion_name} ({promotion_amount})")

                # Display promotion totals
            print("\nPromotion Totals:")
            for promotion_name, total_amount in promotion_totals.items():
                print(f"{promotion_name}: ${total_amount:.2f}")
            if without_promotion_total > 0:
                print(f"Without Promotion: ${without_promotion_total:.2f}")
            elif choice == '4':
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please choose a valid option.\n")
    except Exception as e:
        print("An error occurred:", str(e))



if __name__ == "__main__":
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, max_quantity=1)
                    ]

    # Create promotion catalog
    second_half_price = promotions.SecondProductHalfPrice("Second Half price!")
    third_one_free = promotions.BuyTwoGetOneFree("Third One Free!")
    thirty_percent = promotions.PercentagePromotion("30% off!", percentage=30)

    # Add promotions to products
    product_list[0]. set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = store.Store(product_list)
    start(best_buy)
