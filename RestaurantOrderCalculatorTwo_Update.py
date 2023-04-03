# The menu list contains tuples with the name, price, and description of each entree
menu = [
    ("Linguini With Stuffed Meatballs", 26, "Mozzarella stuffed meatballs, cilantro cream sauce."),
    ("Vegetable Paella", 24, "Roasted seasonal vegetables, mushrooms, sweet potato, organic red quinoa."),
    ("Braised Short Rib Cavatelli", 29, "Baked with mushrooms, pearl onions, whipped ricotta."),
    ("Irish Organic Salmon", 29, "Flemon cous cous, rustic garden vegetables, tomatoes, capers, white wine sauce."),
    ("Teriyaki Chicken", 26, "Organic chicken, jasmine rice, avocado, stir-fried vegetables"),
    ("Rigatoni With Chicken", 26, "Organic chicken, house oven dried tomato cream sauce"),
    ("Lobster Ravioli", 32, "North atlantic lobster, sherry cream sauce"),
    ("Seafood Risotto", 30, "Shrimp, calamari, shellfish broth, vegetable mire poix."),
    ("Sesame Crusted Yellowfin Tuna", 30, "Shaved brussels sprouts, enoki mushrooms, peppers, carrots, soy-ginger broth"),
    ("Blackened Prime Ribeye Steak", 52, "Cast iron seared, 20oz bone in prime ribeye. Sweet potato au gratin.")
]

# The sides list contains tuples with the name and price of each side
sides = [
    ("Chicken Orzo Soup", 8),
    ("Organic Field Greens", 6)
]

# The add_to_order function takes an entree and an optional side, calculates the price, and formats the order
def add_to_order(entree, side=None):
    price = menu[entree-1][1]
    order = "\n" + menu[entree-1][0] + ": $" + str(price)

    if side is not None:
        price += sides[side-1][1]
        order += "\n" + sides[side-1][0] + ": $" + str(sides[side-1][1])

    return price, order

total_price = 0
total_order = ""

# Get user's entree selection
entrees = int(input("Please Select Your Entree (1-10): "))

# Display the selected entree and its price
print(menu[entrees-1][0], "-", menu[entrees-1][2], "\nPrice: $" + str(menu[entrees-1][1]))

# Ask if the user wants to add the entree to their order
y_N = input("Do You Want to Add This to Your order? \nY For Yes N For No: ")

# If the user wants to add the entree to their order, ask for their side selection and update the order
if y_N == "Y":
    side_choice = int(input("Please Select Your Side (1 for Chicken Orzo Soup or 2 for Organic Field Greens): "))
    price, order = add_to_order(entrees, side_choice)
    total_price += price
    total_order += order

# Print the total order and price
print("Total Order:", total_order)
print("Total Price: $" + str(total_price))