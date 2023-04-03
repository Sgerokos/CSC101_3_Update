# Imports the sys package into python
import sys

# Function to add a side to the order
def add_side_choice():
    s = int(input("Do You Want Chicken Orzo Soup or"
                  "\nOrganic Field Greens as a Side"
                  "\nPlease Select 1 For Chicken Orzo Soup"
                  "\nor 2 For Field Greens: "))
    if s == 1:
        yn = input("Do You Want to Add Chicken Orzo Soup as the Side? "
                   "\nY For Yes N For No: ")
        if yn == "Y":
            return "\nChicken Orzo Soup"
    elif s == 2:
        yn = input("Do You Want to Add Chicken Field Greens as the Side? "
                   "\nY For Yes N For No: ")
        if yn == "Y":
            return "\nField Greens"
    return ""

# Entree data with their number, description, and price
entree_data = [
    (1, "Linguini With Stuffed Meatballs - Mozzarella stuffed meatballs,\n"
         "cilantro cream sauce.", 26),
    (2, "Vegetable Paella - Roasted seasonal vegetables, mushrooms,\n"
         "sweet potato, organic red quinoa.", 24),
    (3, "Braised Short Rib Cavatelli - Baked with mushrooms,\n"
         "pearl onions, whipped ricotta.", 29),
    (4, "Irish Organic Salmon - Flemon cous cous, rustic garden vegetables,\n"
         "tomatoes, capers, white wine sauce.", 29),
    (5, "Teriyaki Chicken - Organic chicken, jasmine rice,\n"
         "avocado, stir-fried vegetables.", 26),
    (6, "Rigatoni With Chicken - Organic chicken,\n"
         "house oven dried tomato cream sauce.", 26),
    (7, "Lobster Ravioli - North Atlantic lobster, sherry cream sauce.", 32),
    (8, "Seafood Risotto - Shrimp, calamari, shellfish broth,\n"
         "vegetable mire poix.", 30),
    (9, "Sesame Crusted Yellowfin Tuna - Shaved brussels sprouts,\n"
         "enoki mushrooms, peppers, carrots, soy-ginger broth.", 30),
    (10, "Blackened Prime Ribeye Steak - Cast iron seared,\n"
          "20oz bone in prime ribeye.\nSweet potato au gratin.", 52),
]

## Greet the customer and prompt for their entree choice
print("Hello Welcome to Sanfords Restaurant"
      "\nWhat Can I Serve You Today?")

price = 0
order = ""
sides = ""

while True:
    entrees = int(input("Please Select One of The Following Entrées:"
                        "\n1 For Linguini With Stuffed Meatballs"
                        "\n2 For Vegetable Paella,"
                        "\n3 For Braised Short Rib Cavatelli,"
                        "\n4 For Irish Organic Salmon,"
                        "\n5 For Teriyaki Chicken,"
                        "\n6 For Rigatoni With Chicken,"
                        "\n7 For Lobster Ravioli,"
                        "\n8 For Seafood Risotto"
                        "\n9 For Sesame Crusted Yellowfin Tuna,"
                        "\n10 For Blackened Prime Ribeye Steak: "))

    # Iterate through entree_data to find the matching entree and prompt for adding to order
    for entree_num, entree_desc,entree_price in entree_data:
        if entrees == entree_num:
            print(f"{entree_desc}\nPrice: ${entree_price}")
            y_N = input("Do You Want to Add This to Your order? "
                        "\nY For Yes N For No: ")

            if y_N == "Y":
                price += entree_price
                order += f"\n{entree_desc.split(' - ')[0]}: ${entree_price}"
                sides += add_side_choice()

            elif y_N == "N":
                order += ""

    # Ask if the customer wants to order something else
    something_Else = input("Would You Like Something Else? "
                           "\nPlease Enter Y For Yes or N For No:")

    if something_Else == "N":
        break

sales_Tax = 0.0875
tax = price * sales_Tax
total = price + tax
tips = [(percentage, total * percentage * 0.01) for percentage in range(10, 31, 5)]

# Print the order summary and tips
print("Order's:", order, "\nSide's:", sides,
      "\nTotal Without Tax", price,
      "\nThe Total With Tax is:", round(total, 2),
      "\nThe Sale's Tax is:", round(tax, 2))

for tip_percentage, tip_amount in tips:
    print(f"{tip_percentage}% Tip is:", round(tip_amount, 2))

sys.exit()