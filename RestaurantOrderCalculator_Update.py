import sys

# Welcome the user to the restaurant
print("Hello! Welcome to Sanfords Restaurant"
      "\nWhat can I serve you today?")

# Set the sales tax to 8.75%
sales_tax = 0.0875

# Initialize the price variable to 0
price = 0

# Set the add_more_items variable to "Y" until the user changes it
add_more_items = "Y"

# Keep looping while the user wants to add more items
while add_more_items == "Y":
    
    # Ask the user to input a number for one of the items
    entrees = int(input("Please select one of the following entrées:"
                        "\n1 for Linguini With Stuffed Meatballs"
                        "\n2 for Vegetable Paella,"
                        "\n3 for Braised Short Rib Cavatelli,"
                        "\n4 for Irish Organic Salmon,"
                        "\n5 for Teriyaki Chicken,"
                        "\n6 for Rigatoni With Chicken,"
                        "\n7 for Lobster Ravioli,"
                        "\n8 for Seafood Risotto"
                        "\n9 for Sesame Crusted Yellowfin Tuna,"
                        "\n10 for Blackened Prime Ribeye Steak: "))

    # Add the selected item's price to the total price
    if entrees == 1:
        print("Linguini With Stuffed Meatballs - Mozzarella stuffed meatballs," 
              "\ncilantro cream sauce." 
              "\nPrice: $26")
        price += 26
    # Other cases for each entree...
    # ...
    # Check if the user wants to add more items
    add_more_items = input("Would you like something else?"
                           "\nPlease enter Y for Yes or N for No:")

    if add_more_items == "N":
        # Calculate the tax, total, and recommended tips
        tax = price * sales_tax
        total = price + tax
        tips = {10: total * 0.10,
                15: total * 0.15,
                20: total * 0.20,
                25: total * 0.25,
                30: total * 0.30}

        # Print the total, tax, and recommended tips
        print(f"The total is: ${round(total, 2)}"
              f"\nThe sales tax is: ${round(tax, 2)}")
        
        for tip_percentage, tip_amount in tips.items():
            print(f"{tip_percentage}% tip is: ${round(tip_amount, 2)}")

        sys.exit()

    # If an invalid input is entered, show an error message
    elif add_more_items != "Y" and add_more_items != "N":
        print(f"Invalid input: {add_more_items}")
    elif entrees < 1 or entrees > 10:
        print("Invalid number for entrées. Please enter a number between 1 - 10 for this selection.")