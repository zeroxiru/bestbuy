import store
import products


def start(store_obj):
    """
    Display the store menu and handles the user interactions.

    Args:
        store_obj is a list of store object which represents the store inventory.
    """
    try:
        while True:
            print("Store Menu\n----------")
            print("1. List all products in store")
            print("2. Show total amount in store")
            print("3. Make an order")
            print("4. Quit")

            choice = input("Please choose a number: ")

            if choice == "1":
                for idx, product in enumerate(store_obj.get_all_products(), start=1):
                    print(f"{idx}. Name: ${product._name}, Price: {product._price}, Quantity: {product._quantity} ")
            elif choice == "2":
                total_quantity = store_obj.get_total_quantity()
                print(f'Total amount of quantity in store: {total_quantity}')

            elif choice == '3':
                print("------")
                products = store_obj.get_all_products()
                for idx, product in enumerate(products, start=1):
                    print(f'{idx}. Name:{product._name}, Price:{product._price}, Quantity:{product._quantity}')
                print("------")

                order_list = []
                while True:
                    product_num = input("Which product # do you want? ")
                    if not product_num:
                        break
                    product_num = int(product_num) - 1  # Adjust for 0-based indexing
                    selected_product = store_obj.get_all_products()[product_num]
                    amount = int(input("What amount do you want? "))
                    if amount != 0 and amount <= selected_product._quantity:
                        order_list.append((store_obj.get_all_products()[product_num], amount))
                    else:
                        print(f" Given product: {selected_product._name} amount is more than storage quantity")
                    #if selected_product.


                print("Product added to list!\n")

                total_payment = store_obj.order(order_list)
                print("********")
                print(f"Order made! Total payment: ${total_payment}")
            elif choice == '4':
                print("Goodbye!")
                break  # Correct indentation for the break statement

            else:
                print("Invalid choice. Please choose a valid option.\n")
    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    # Setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=50)
    ]

    best_buy = store.Store(product_list)
    start(best_buy)
