# Import the sys package into python
import sys

# Define constants for sales tax and tip percentages
SALES_TAX = 0.0875
TIPS = [0.10, 0.15, 0.20, 0.25, 0.30]

MENU_ITEMS = [
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

MENU_PRICES = [26.00, 24.00, 29.00, 29.00, 26.00, 26.00, 32.00, 30.00, 30.00, 52.00]
SIDES = ["Chicken Orzo Soup", "Field Greens"]

def subTotal(order, quantities, prices, sides):
    total_no_tax = sum(prices[i]*quantities[i] for i in range(len(prices)))
    tax = total_no_tax * SALES_TAX
    total_with_tax = total_no_tax + tax
    tip_amounts = [total_with_tax * tip for tip in TIPS]

    for item, price, quantity, side in zip(order, prices, quantities, sides):
        print(f"Order: {item} Price: ${price:.2f} Quantity: {quantity} Side: {side}")

    print(f"Total Without Tax: ${total_no_tax:.2f} Total With Tax: ${total_with_tax:.2f} The Total is: ${total_with_tax:.2f} Sale's Tax is: ${tax:.2f}")
    for i, tip in enumerate(tip_amounts):
        print(f"{int(TIPS[i]*100)}% Tip is: ${tip:.2f}")

def get_side():
    print("Do You Want Chicken Orzo Soup or Organic Field Greens as a Side")
    s = int(input("Please Select 1 For Chicken Orzo Soup or 2 For Field Greens: ")) - 1
    return SIDES[s]

def yes_no_prompt(prompt):
    while True:
        response = input(prompt).upper()
        if response in ["Y", "N"]:
            return response == "Y"

def order_quantity_prompt():
    return int(input("\nHow Many Order's Would You Enjoy: "))  

def confirmation_prompt():
    return yes_no_prompt("Do You Want to Add This to Your order? Y for Yes N for No: ")

def display_menu():
    for i, (item, price) in enumerate(zip(MENU_ITEMS, MENU_PRICES), 1):
        print(f"{i} For: {item} Price: ${price:.2f}")

def get_order():
    order = []
    quantities = []
    prices = []
    sides = []

    while True:
        display_menu()
        selection = int(input("\nPlease Select One of The Following Entrees : ")) - 1

        if confirmation_prompt():
            quantity = order_quantity_prompt()
            side = get_side()

            order.append(MENU_ITEMS[selection])
            quantities.append(quantity)
            prices.append(MENU_PRICES[selection])
            sides.append(side)

        if not yes_no_prompt("Would You Like Something Else? Please Enter Y For Yes or N For No:"):
            break

    return order, quantities, prices, sides

def main():
    print("\nHello Welcome to Sanfords Restaurant\n\nWhat Can I Serve You Today?\n\nMenu:")

    order, quantities, prices, sides = get_order()
    subTotal(order, quantities, prices, sides)

    sys.exit()

if __name__ == "__main__":
    main()