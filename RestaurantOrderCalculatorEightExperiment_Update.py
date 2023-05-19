# Global constants
SALES_TAX = 0.0875
TIP_RATES = [0.10, 0.15, 0.20, 0.25, 0.30]
MENU_ITEMS = [
    "Linguini With Stuffed Meatballs",
    "Vegetable Paella",
    "Braised Short Rib Cavatell",
    "Irish Organic Salmon",
    "Teriyaki Chicken",
    "Rigatoni With Chicken",
    "Lobster Ravioli",
    "Seafood Risotto",
    "Sesame Crusted Yellowfin Tuna",
    "Blackened Prime Ribeye Steak"
]
MENU_PRICES = [26.00, 24.00, 29.00, 29.00, 26.00, 26.00, 32.00, 30.00, 30.00, 52.00]
SIDES = ["Chicken Orzo Soup", "Field Greens"]

# Variables to hold the current order details
order = []
quantities = []
prices = []
sides = []


def display_menu():
    """Display the menu items along with their prices."""
    for idx, (item, price) in enumerate(zip(MENU_ITEMS, MENU_PRICES)):
        print(f"{idx + 1} For: {item} Price: ${price}")


def get_user_choice(prompt, valid_choices):
    """Ask the user to make a choice and validate their input."""
    while True:
        try:
            choice = int(input(prompt))
            if choice not in valid_choices:
                raise ValueError
            return choice
        except ValueError:
            print(f"Invalid input. Please enter one of the following options: {valid_choices}")


def add_to_order(entree_idx, quantity, side_idx):
    """Add an entree to the order, along with its quantity and side dish."""
    order.append(MENU_ITEMS[entree_idx])
    quantities.append(quantity)
    prices.append(MENU_PRICES[entree_idx])
    sides.append(SIDES[side_idx])


def display_order():
    """Display the current order, along with the subtotal, tax, total, and suggested tips."""
    print("\nYour order:")
    subtotal = sum(prices[i] * quantities[i] for i in range(len(order)))
    tax = round(subtotal * SALES_TAX, 2)
    total = round(subtotal + tax, 2)

    for item, quantity, side, price in zip(order, quantities, sides, prices):
        print(f"Order: {item} Quantity: {quantity} Side: {side} Price: ${price * quantity}")

    print(f"\nSubtotal: ${subtotal}")
    print(f"Sales tax: ${tax}")
    print(f"Total with tax: ${total}")

    for tip_rate in TIP_RATES:
        tip = round(total * tip_rate, 2)
        print(f"{int(tip_rate * 100)}% tip: ${tip}")


def main():
    print("\nHello, welcome to Sanford's Restaurant. What can I serve you today?\n")

    while True:
        display_menu()

        entree_idx = get_user_choice("\nPlease select one of the following entrees: ",
                                     range(1, len(MENU_ITEMS) + 1)) - 1
        quantity = get_user_choice("\nHow many orders would you enjoy: ", range(1, 101))
        side_idx = get_user_choice("\nPlease select a side (1 for Chicken Orzo Soup, 2 for Field Greens): ", [1, 2]) - 1

        add_to_order(entree_idx, quantity, side_idx)

        another_item = input("\nWould you like to order something else? Enter Y for Yes or N for No: ").upper()
        if another_item == 'N':
            break
        elif another_item != 'Y':
            print("Invalid input. Please enter either 'Y' or 'N'.")

    display_order()


if __name__ == "__main__":
    main()