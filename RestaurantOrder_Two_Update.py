# Define a variable for sales tax
sales_tax = 0.07

# Define variables to keep track of the order
order = ""
sides = ""

# Define variables to keep track of the price and the total
price = 0.0
total = 0.0

# Define a function to ask for user input and validate it
def get_input(message, valid_options):
    while True:
        user_input = input(message)
        if user_input in valid_options:
            return user_input
        else:
            print("Invalid input, please try again.")

# Define a function to add an item to the order
def add_item(name, item_price):
    global order, price
    print(name, "- Price: ${:.2f}".format(item_price))
    yn = get_input("Do you want to add this to your order? (Y/N) ", ["Y", "N"])
    if yn == "Y":
        order += "\n" + name + ": ${:.2f}".format(item_price)
        price += item_price

# Define the menu items
menu_items = {
    1: ("Linguini With Stuffed Meatballs", 15.50),
    2: ("Vegetable Paella", 19.00),
    3: ("Braised Short Rib Cavatelli", 22.00),
    4: ("Irish Organic Salmon", 26.00),
    5: ("Teriyaki Chicken", 18.00),
    6: ("Rigatoni With Chicken", 16.50),
    7: ("Lobster Ravioli", 28.00),
    8: ("Seafood Risotto", 30.00),
    9: ("Sesame Crusted Yellowfin Tuna", 30.00),
    10: ("Blackened Prime Ribeye Steak", 52.00)
}

# Display the menu and ask for user input
entree = -1
while entree != 0:
    print("Menu:")
    for key, value in menu_items.items():
        print("{}: {} - Price: ${:.2f}".format(key, value[0], value[1]))
    entree = int(input("Please select an entree (1-10) or enter 0 if you are finished ordering: "))
    if entree == 0:
        break
    elif entree not in menu_items:
        print("Invalid input, please try again.")
        continue

    # Add the selected item to the order
    name, item_price = menu_items[entree]
    add_item(name, item_price)

    # Ask for a side if applicable
    if entree in [4, 5, 6, 9, 10]:
        print("Sides:")
        print("1: Chicken Orzo Soup - Price: $4.50")
        print("2: Organic Field Greens - Price: $4.00")
    s = get_input("Please select a side (1-2) or enter 0 if you do not want a side: ", ["1", "2", "0"])

    if s == "1":
        yn = get_input("Do you want to add Chicken Orzo Soup as the side? (Y/N) ", ["Y", "N"])
        if yn == "Y":
            sides += "\nChicken Orzo Soup"
    elif s == "2":
        yn = get_input("Do you want to add Organic Field Greens as the side? (Y/N) ", ["Y", "N"])

        if yn == "Y":
            sides += "\nOrganic Field Greens"

# Calculate the tax and total
tax = price * sales_tax
total = price + tax

# Calculate the tip amounts
ten_Tip = total * 0.10
fifteen_Tip = total * 0.15
twenty_Tip = total * 0.20
twenty_Five_tip = total * 0.25
thirty_Tip = total * 0.30

# Print the order summary and recommended tips
print("Order:", order)
print("Sides:", sides)
print("Total without tax: ${:.2f}".format(price))
print("Total with tax: ${:.2f}".format(total))
print("Sales tax: ${:.2f}".format(tax))
print("Recommended Tips:")
print("- 10%: ${:.2f}".format(ten_Tip))
print("- 15%: ${:.2f}".format(fifteen_Tip))
print("- 20%: ${:.2f}".format(twenty_Tip))
print("- 25%: ${:.2f}".format(twenty_Five_tip))
print("- 30%: ${:.2f}".format(thirty_Tip))