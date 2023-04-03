import sys

# Calculates the subtotal, tax, and total amount
def subTotal(price, order, sides):
    sales_tax_rate = 0.0875
    tax = price * sales_tax_rate
    total = price + tax

    tip_percentages = [0.10, 0.15, 0.20, 0.25, 0.30]
    tips = [total * percentage for percentage in tip_percentages]

    print("Orders:", *order, "\nSides:", *sides,
          "\nTotal Without Tax:", price,
          "\nThe Total With Tax is:", round(total, 2),
          "\nThe Sales Tax is:", round(tax, 2))

    for i, tip in enumerate(tips):
        print(f"{int(tip_percentages[i] * 100)}% Tip is:", round(tip, 2))

    sys.exit()

# Gets the user's side choice
def get_side_choice():
    sides = ["Chicken Orzo Soup", "Field Greens"]

    print("Please select a side:")
    for i, side in enumerate(sides, start=1):
        print(f"{i}. {side}")

    choice = int(input())

    if 1 <= choice <= len(sides):
        selected_side = sides[choice - 1]
    else:
        print("Invalid choice. Please try again.")
        return get_side_choice()

    return selected_side

# Asks if the user wants to add more items
def ask_for_more_items():
    user_choice = input("Would you like something else? (Y/N): ")

    if user_choice.upper() == "Y":
        return True
    elif user_choice.upper() == "N":
        return False
    else:
        print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
        return ask_for_more_items()

# Gets the user's choice for an entree
def get_user_choice():
    print("\nHello! Welcome to Sanfords Restaurant"
          "\n\nWhat can I serve you today?"
          "\n\nMenu:"
          "\n\n1: Linguini with Stuffed Meatballs - Mozzarella stuffed meatballs, cilantro cream sauce. Price: $26"
          "\n2: Vegetable Paella - Roasted seasonal vegetables, mushrooms, sweet potato, organic red quinoa. Price: $24"
          "\n3: Braised Short Rib Cavatelli - Baked with mushrooms, pearl onions, whipped ricotta. Price: $29"
          "\n4: Irish Organic Salmon - Lemon couscous, rustic garden vegetables, tomatoes, capers, white wine sauce. Price: $29"
          "\n5: Teriyaki Chicken - Organic chicken, jasmine rice, avocado, stir-fried vegetables. Price: $26"
          "\n6: Rigatoni with Chicken - Organic chicken, house oven dried tomato cream sauce. Price: $26"
          "\n7: Lobster Ravioli - North Atlantic lobster, sherry cream sauce. Price: $32"
          "\n8: Seafood Risotto - Shrimp, calamari, shellfish broth, vegetable mirepoix. Price: $30"
          "\n9: Sesame Crusted Yellowfin Tuna - Shaved brussels sprouts, enoki mushrooms, peppers, carrots, soy-ginger broth. Price: $30"
          "\n10: Blackened Prime Ribeye Steak - Cast iron seared, 20oz bone-in prime ribeye. Sweet potato au gratin. Price: $52"
          "\n\nPlease select one of the following entrees:")

    user_choice = int(input())

    return user_choice


# Processes the order, adding items to the order and calculating the total price
def process_order(entrees):
    menu_items = ["Linguini With Stuffed Meatballs", "Vegetable Paella",
                  "Braised Short Rib Cavatelli", "Irish Organic Salmon",
                  "Teriyaki Chicken", "Rigatoni With Chicken", "Lobster Ravioli",
                  "Seafood Risotto", "Sesame Crusted Yellowfin Tuna",
                  "Blackened Prime Ribeye Steak"]

    menu_prices = [26.00, 24.00, 29.00, 29.00, 26.00, 26.00,
                   32.00, 30.00, 30.00, 52.00]

    order = []
    sides = []
    total_price = 0

    while entrees != 0:
        if 1 <= entrees <= 10:
            item_price = menu_prices[entrees - 1]
            item_name = menu_items[entrees - 1]

            confirmation = input(f"Do you want to add {item_name} to your order? "
                                 "\nY for Yes, N for No: ")

            if confirmation.upper() == "Y":
                total_price += item_price
                order.append(item_name)
                sides.append(get_side_choice())

                if ask_for_more_items():
                    entrees = get_user_choice()
                else:
                    entrees = 0

            elif confirmation.upper() == "N":
                entrees = get_user_choice()
            else:
                print("Invalid input. Please enter Y for Yes or N for No.")
        else:
            print("\nYou have entered an invalid number for the entrees"
                  "\nPlease enter a number between 1 - 10 for this selection")
            entrees = get_user_choice()

    return total_price, order, sides


def main():
    entrees = get_user_choice()
    price, order, sides = process_order(entrees)
    subTotal(price, order, sides)


main()