# Menu items and their corresponding prices
menu_items = [
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
menu_prices = [26.00, 24.00, 29.00, 29.00, 26.00, 26.00, 32.00, 30.00, 30.00, 52.00]

# Current order details
order = []
total_price = 0

# Display the menu items along with their prices
for i, (item, price) in enumerate(zip(menu_items, menu_prices), 1):
    print(f"{i}. {item} - ${price}")

# Ask the customer to choose an item until they decide to stop
while True:
    try:
        choice = int(input("\nPlease enter the number of the dish you'd like to order (or 0 to finish ordering): "))
        if choice == 0:
            break
        elif 1 <= choice <= len(menu_items):
            order.append(menu_items[choice-1])
            total_price += menu_prices[choice-1]
            print(f"\nYou've added {menu_items[choice-1]} to your order. Current total price is ${total_price:.2f}.")
        else:
            print("\nInvalid input. Please enter a number corresponding to a dish.")
    except ValueError:
        print("\nInvalid input. Please enter a number.")

# Display the final order and total price
print("\nYour order:")
for item in order:
    print(f" - {item}")
print(f"Total price: ${total_price:.2f}")