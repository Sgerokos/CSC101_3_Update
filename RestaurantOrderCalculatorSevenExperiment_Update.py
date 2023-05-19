# This function returns a list of menu items
def get_menu_items():
    return [
        "Linguini With Stuffed Meatballs",
        "Vegetable Paella",
        "Braised Short Rib Cavatelli",
        "Irish Organic Salmon",
        "Teriyaki Chicken",
        "Rigatoni With Chicken",
        "Lobster Ravioli",
        "Seafood Risotto",
        "Sesame Crusted Yellowfin Tuna",
        "Blackened Prime Ribeye Steak"
    ]

# This function returns a list of menu prices
def get_menu_prices():
    return [26.00, 24.00, 29.00, 29.00, 26.00, 26.00, 32.00, 30.00, 30.00, 52.00]

# The main function orchestrates the overall flow of the program
def main():
    menu_items = get_menu_items()
    menu_prices = get_menu_prices()

    # Display the menu to the user
    for i, (item, price) in enumerate(zip(menu_items, menu_prices), 1):
        print(f"{i}. {item} - ${price:.2f}")

    # Ask the user for their choice and add it to the orders
    orders = []
    user_input = int(input("Please enter the number of the dish you'd like to order: "))
    if 1 <= user_input <= len(menu_items):
        orders.append(menu_items[user_input - 1])
        print(f"You've ordered: {menu_items[user_input - 1]} for ${menu_prices[user_input - 1]:.2f}")
    else:
        print("Invalid input. Please enter a number corresponding to a dish.")

    print("Your orders:", orders)

# Run the main function
main()