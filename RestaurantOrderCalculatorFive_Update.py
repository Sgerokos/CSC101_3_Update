# Menu items, descriptions, and prices
MENU_ITEMS = {
    "Linguini With Stuffed Meatballs": 26.00,
    "Vegetable Paella": 24.00,
    "Braised Short Rib Cavatelli": 29.00,
    "Irish Organic Salmon": 29.00,
    "Teriyaki Chicken": 26.00,
    "Rigatoni With Chicken": 26.00,
    "Lobster Ravioli": 32.00,
    "Seafood Risotto": 30.00,
    "Sesame Crusted Yellowfin Tuna": 30.00,
    "Blackened Prime Ribeye Steak": 52.00
}

# Side options
SIDES = ["Chicken Orzo Soup", "Field Greens"]

# Sales tax rate
SALES_TAX_RATE = 0.0875

# Possible tips
TIP_PERCENTAGES = [0.10, 0.15, 0.20, 0.25, 0.30]


def calculate_subtotal(order_price):
    tax = order_price * SALES_TAX_RATE
    total = order_price + tax
    tips = [total * tip_percentage for tip_percentage in TIP_PERCENTAGES]

    return total, tax, tips


def choose_side():
    print("Do you want Chicken Orzo Soup or Organic Field Greens as a side?")
    s = int(input("Please select 1 for Chicken Orzo Soup or 2 for Field Greens: "))
    chosen_side = SIDES[s - 1]
    return chosen_side


def yes_no_prompt(prompt):
    while True:
        response = input(prompt).upper()
        if response in ["Y", "N"]:
            return response == "Y"


def user_input():
    print("\nHello, welcome to Sanfords Restaurant. What can I serve you today?")
    for i, (item, price) in enumerate(MENU_ITEMS.items(), 1):
        print(f"\n{i} For {item} - Price: ${price}")

    item_choice = int(input("\nPlease select one of the following entrees: ")) - 1
    chosen_item = list(MENU_ITEMS.keys())[item_choice]
    chosen_price = list(MENU_ITEMS.values())[item_choice]

    if yes_no_prompt("Would you like to add this to your order? (Y for Yes, N for No): "):
        return chosen_item, chosen_price
    else:
        return None, None


def main():
    total_price = 0
    all_orders = []

    while True:
        item, price = user_input()
        if item is None:
            break

        all_orders.append(item)
        total_price += price

        side_order = choose_side()
        all_orders.append(side_order)  # Side order also added to the total order list

        if not yes_no_prompt("Would you like something else? (Y for Yes, N for No): "):
            break

    total, tax, tips = calculate_subtotal(total_price)

    print(f"\nOrder's: {all_orders}\nTotal Without Tax: ${total_price}\nTotal With Tax: ${total}\nTax: ${tax}")
    for i, tip in enumerate(tips, 1):
        print(f"Total with {TIP_PERCENTAGES[i - 1] * 100}% tip: ${total + tip:.2f}")


# Run the main function to start the program.
main()
