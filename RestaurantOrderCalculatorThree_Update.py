# Define the menu items and prices as lists
menu_items = ["Linguini With Stuffed Meatballs",
              "Vegetable Paella",
              "Braised Short Rib Cavatelli",
              "Irish Organic Salmon",
              "Teriyaki Chicken",
              "Rigatoni With Chicken",
              "Lobster Ravioli",
              "Seafood Risotto",
              "Sesame Crusted Yellowfin Tuna",
              "Blackened Prime Ribeye Steak"]
prices = [26, 24, 29, 29, 26, 26, 32, 30, 30, 52]

# Define the menu and side dish variables as dictionaries
menu = {"price": 0, "order": ""}
side = {"sides": ""}

def subTotal(price):
    # Set the sales tax rate
    sales_tax_rate = 0.0875
    # Calculate the tax amount based on the price
    tax = price * sales_tax_rate

    # Add the tax amount to the price to get the final total
    total = price + tax

    # Print the subtotal, tax amount, and total
    print("\nSubtotal:", price,
          "\nTax:", round(tax, 2),
          "\nTotal:", round(total, 2))

    # Ask the user if they want to add a tip
    tip = input("\nWould you like to leave a tip? Y for Yes, N for No: ")

    # If the user wants to add a tip, calculate and print the recommended tip amounts
    if tip.lower() == "y":
        ten_percent_tip = total * 0.10
        fifteen_percent_tip = total * 0.15
        twenty_percent_tip = total * 0.20
        twenty_five_percent_tip = total * 0.25
        thirty_percent_tip = total * 0.30
        print("\n10% tip:", round(ten_percent_tip, 2),
              "\n15% tip:", round(fifteen_percent_tip, 2),
              "\n20% tip:", round(twenty_percent_tip, 2),
              "\n25% tip:", round(twenty_five_percent_tip, 2),
              "\n30% tip:", round(thirty_percent_tip, 2))
    elif tip.lower() != "n":
        print("Invalid input. Please enter Y or N.")
        subTotal(price)

def subTotal(price):
    # Set the sales tax rate
    sales_tax_rate = 0.0875
    # Calculate the tax amount based on the price
    tax = price * sales_tax_rate

    # Add the tax amount to the price to get the final total
    total = price + tax

    # Print the subtotal, tax amount, and total
    print("\nSubtotal:", price,
          "\nTax:", round(tax, 2),
          "\nTotal:", round(total, 2))

    # Ask the user if they want to add a tip
    tip = input("\nWould you like to leave a tip? Y for Yes, N for No: ")

    # If the user wants to add a tip, calculate and print the recommended tip amounts
    if tip.lower() == "y":
        ten_percent_tip = total * 0.10
        fifteen_percent_tip = total * 0.15
        twenty_percent_tip = total * 0.20
        twenty_five_percent_tip = total * 0.25
        thirty_percent_tip = total * 0.30
        print("\n10% tip:", round(ten_percent_tip, 2),
              "\n15% tip:", round(fifteen_percent_tip, 2),
              "\n20% tip:", round(twenty_percent_tip, 2),
              "\n25% tip:", round(twenty_five_percent_tip, 2),
              "\n30% tip:", round(thirty_percent_tip, 2))
    elif tip.lower() != "n":
        print("Invalid input. Please enter Y or N.")
        subTotal(price)

def add_side():
    # Initialize the sides variable
    sides = ""

    # Ask the user to choose a side dish
    side_choice = input(
        "Do you want Chicken Orzo Soup or Organic Field Greens as a side? Please select 1 for Chicken Orzo Soup or 2 for Organic Field Greens: ")

    # If the user selects Chicken Orzo Soup
    if side_choice == "1":
        # Ask if they want to add it to their order
        add_side = input("Do you want to add Chicken Orzo Soup as a side? Y for Yes, N for No: ")

        # If the user selects yes, add the side to the order
        if add_side.lower() == "y":
            sides += "Chicken Orzo Soup"

    # If the user selects Organic Field Greens
    elif side_choice == "2":
        # Ask if they want to add it to their order
        add_side = input("Do you want to add Organic Field Greens as a side? Y for Yes, N for No: ")

        # If the user selects yes, add the side to the order
        if add_side.lower() == "y":
            sides += "\nOrganic Field Greens"

    # If the user selects an invalid option
    else:
        print("Invalid choice. Please select 1 for Chicken Orzo Soup or 2 for Organic Field Greens.")

    return sides

def yesNo():
    # Ask the user if they want to add more items to their order
    something_else = input("Would you like to order something else? "
    "\nPlease enter Y for Yes or N for No: ")
    # If the user wants to add more items, call the userInput function
    if something_else.lower() == "y":
        main()

    # If the user is done ordering, calculate the subtotal and exit the program
    elif something_else.lower() == "n":
        subTotal(menu["price"])

    # If the user inputs something other than Y or N, print an error message and call the userInput function again
    else:
        print("Invalid input. Please enter Y or N.")

def userInput():
    # Welcome message for the user
    print("Welcome to Sanford's Restaurant. What can I serve you today?")
    # Display menu items for the user to choose from
    print("Please select one of the following entrées:")
    for i, item in enumerate(menu_items):
        print(f"{i + 1}. {item} - ${prices[i]}")

    # Get the user's input for their selected menu item
    while True:
        e = input("Enter the number of your selected entrée: ")
        if e.isdigit() and 1 <= int(e) <= len(menu_items):
            return int(e)
        else:
            print("Invalid input. Please enter a number between 1 and", len(menu_items))

def order_menu(entree):
    # Loop until the user selects 0 to finish ordering
    while entree != 0:
        if entree < 1 or entree > len(menu_items):
            # If an invalid number is selected, print an error message
            print("\nInvalid selection. Please enter a number between 1 and", len(menu_items))
        else:
            # Print the details of the selected entree
            print(f"{menu_items[entree-1]} - ${prices[entree-1]}")
            # Ask the user if they want to add this entree to their order
            yn = input("Do you want to add this to your order? (Y/N) ")

            if yn == "Y":
                # Add the price and name of the entree to the variables
                menu["price"] += prices[entree - 1]
                menu["order"] += f"\n{menu_items[entree - 1]}: ${prices[entree - 1]}"

                # Ask the user if they want a side dish
                side["sides"] += add_side()

            # If the user doesn't want to add the entree to their order, do nothing
            elif yn == "N":
                pass

            # Ask the user for the next entree or if they're finished
            entree = int(input("Please select an entree (1-10) or enter 0 to finish: "))

    # Once the user is finished, ask if they want to order something else or see their subtotal
    yesNo()

def main():
    entrees = userInput()
    order_menu(entrees)

main()