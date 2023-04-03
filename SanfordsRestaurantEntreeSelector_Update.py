# Welcome the user to the restaurant
print("Hello! Welcome to Sanfords Restaurant.")
print("What can I serve you today?")

# Define the menu as a dictionary with items as keys and prices as values
menu = {
    "Linguini With Stuffed Meatballs": 26,
    "Vegetable Paella": 24,
    "Braised Short Rib Cavatelli": 29,
    "Irish Organic Salmon": 29,
    "Teriyaki Chicken": 17.68,
    "Rigatoni With Chicken": 26,
    "Lobster Ravioli": 32,
    "Seafood Risotto": 30,
    "Sesame Crusted Yellowfin Tuna": 30,
    "Blackened Prime Ribeye Steak": 52,
}

# Loop until the user enters a valid input
while True:
    try:
        # Ask the user to select an entrée
        entrees = int(input("Please select an entrée:\n"
                            "1. Linguini With Stuffed Meatballs\n"
                            "2. Vegetable Paella\n"
                            "3. Braised Short Rib Cavatelli\n"
                            "4. Irish Organic Salmon\n"
                            "5. Teriyaki Chicken\n"
                            "6. Rigatoni With Chicken\n"
                            "7. Lobster Ravioli\n"
                            "8. Seafood Risotto\n"
                            "9. Sesame Crusted Yellowfin Tuna\n"
                            "10. Blackened Prime Ribeye Steak\n"))
        # Check if the input is a valid menu option
        if 1 <= entrees <= 10:
            # Get the selected menu item and price from the dictionary
            item = list(menu.keys())[entrees-1]
            price = menu[item]
            # Print the selected menu item and price
            print(f"{item} - Price: ${price:.2f}")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 10.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 10.")