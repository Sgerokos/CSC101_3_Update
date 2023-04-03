# Imports the sys package into python
import sys


def subTotal():
    # Define the sales tax rate
    sales_tax_rate = 0.0875

    # Calculate the total of sides times quantity
    total_sides = sum(side_price * quantity
                      for side_price, quantity in zip(main.sides_Price, main.ordered_Quantity))

    # Calculate the total of main dish times quantity
    total_main = sum(price * quantity
                     for price, quantity in zip(main.price, main.ordered_Quantity))

    # Calculate the total of main dish and sides
    total = total_main + total_sides

    # Calculate tax as the product of total and sales tax, rounded to the nearest cent
    tax = round(total * sales_tax_rate, 2)

    # Calculate total with no tax, rounded to the nearest cent
    total_no_tax = round(total, 2)

    # Calculate total with tax, rounded to the nearest cent
    total_with_tax = round(total + tax, 2)

    # List recommended tip amounts as the product of total with tax and tip percentage, rounded to the nearest cent
    tip_percentages = [0.10, 0.15, 0.20, 0.25, 0.30]
    tip_amounts = [round(total_with_tax * p, 2) for p in tip_percentages]

    # Print the order details
    for order, price, quantity, side, side_price in zip(main.order, main.price, main.ordered_Quantity, main.sides,
                                                        main.sides_Price):
        print(f"Order: {order} Main Dish Price: ${price:.2f} Quantity: {quantity} "
              f"Side: {side} Side Order Price: ${side_price:.2f}")

    # Print the totals and tax
    print(f"Total Without Tax: ${total_no_tax:.2f} Total With Tax: ${total_with_tax:.2f} "
          f"The Total is: ${total_with_tax:.2f} Sales Tax is: ${tax:.2f}")

    # Print the recommended tip amounts
    for p, tip in zip(tip_percentages, tip_amounts):
        print(f"Percent Tip is: {p:.0%} Tip Amount is: ${tip:.2f}")

    # Exit the program
    sys.exit()

def side():
    # Initialize lists to hold the available sides, their corresponding numbers, and prices
    sides = []
    side_nums = []
    side_prices = []

    # Read in the data from the sides file and populate the lists
    with open('sides.txt', 'r') as f:
        for line in f:
            # Split each line by the delimiter
            parts = line.strip().split("'")

            # Get the number, name, and price of the side
            num = int(parts[0])
            name = parts[1]
            price = int(parts[2])

            # Append the data to the corresponding lists
            side_nums.append(num)
            sides.append(name)
            side_prices.append(price)

    # Print out the available sides with their corresponding numbers and prices
    print("Available Sides:")
    for num, side, price in zip(side_nums, sides, side_prices):
        print("%d. %s ($%.2f)" % (num, side, price))

    # Prompt the user to select a side
    selection = int(input("Enter the number of the side you want: "))

    # Find the index of the selected side in the side_nums list
    index = side_nums.index(selection)

    # Add the selected side and its price to the corresponding lists in the main module
    main.sides.append(sides[index])
    main.sides_Price.append(side_prices[index])

    # Return the updated lists
    return main.sides, main.sides_Price

def yesNo():
    # Ask user if they want to order something else
    choice = input("\nWould you like to order something else? (Y/N): ").strip().lower()

    while choice not in ('y', 'n'):
        try:
            # Handle invalid input
            choice = input("Invalid input! Please enter 'Y' or 'N': ").strip().lower()
        except KeyboardInterrupt:
            # Handle keyboard interrupt (e.g. Ctrl+C)
            print("\nGoodbye!")
            sys.exit()

    if choice == 'y':
        menu()
    else:
        subTotal()

def ordered_Quantity(item_name):
    while True:
        try:
            amount = int(input(f"How many {item_name} would you like to order? "))
            if amount <= 0:
                print("Please enter a positive number.")
            else:
                main.ordered_Quantity.append(amount)
                print(f"{amount} {item_name}(s) added to your order.\n")
                return
        except ValueError:
            print("Please enter a valid integer.")

def confirmation(menu_num, menu_items, menu_prices):
    # Ask the user if they want to add the current order to the total order
    add_to_order = input("\nDo you want to add this item to your order? (Y/N) ").lower()

    # Handle valid user input
    if add_to_order == "y":
        # Find the index of the selected menu item
        index = menu_num.index(menu.entrees)

        # Add the price and item to the order list
        main.price.append(menu_prices[index])
        main.order.append(menu_items[index])

        # Ask for the ordered quantity and side
        ordered_Quantity()
        side()

        return main.order, main.price

    # Handle valid user input
    elif add_to_order == "n":
        # Add empty strings to order list
        main.order.append("")
        main.price.append(0)

        return main.order, main.price

    # Handle invalid user input
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")
        return confirmation(menu_num, menu_items, menu_prices)

def menu():
    # Variables containing lists for order's
    menu.menu_Items = []
    menu.menu_Prices = []
    menu.ordered_Items = []
    menu.ordered_Quantity = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                             11, 12, 13, 14, 15, 16, 17, 18, 19]

    # Load's the Menu.txt data and reads the lines as a list
    with open('Menu.txt', 'r') as menu_file:
        # For loop to read line's
        for menu_info in menu_file:
            # Splits the menu into a list separated by '
            menu_info_as_list = menu_info.split("'")

            # Variables to contain each item
            menu_number = int(menu_info_as_list[0])
            menu_order = menu_info_as_list[1].strip()
            menu_price = int(menu_info_as_list[2])

            # Append's items to the corresponding lists
            menu.ordered_Items.append(menu_number)
            menu.menu_Items.append(menu_order)
            menu.menu_Prices.append(menu_price)

    # Print's the lists
    for col_a, col_b, col_c in \
            zip(menu.ordered_Items, menu.menu_Items, menu.menu_Prices):
        print("%d For: %s Price: $%d" % (col_a, col_b, col_c))

    menu.entrees = userInput()

    # Check if the input is within the valid range
    if menu.entrees not in range(1, 21):
        print("Invalid input.")
        menu()
        return

    # Call confirmation function with the selected entree number
    confirmation(menu.entrees)

    # Prompt for additional orders
    yesNo()

    return menu.entrees

# Defines the function userInput
def userInput():
    # Print out the available entrées with their corresponding numbers and prices
    print("Available Entrées:")
    for num, dish, price in zip(menu.ordered_Items, menu.menu_Items, menu.menu_Prices):
        print("%d. %s ($%.2f)" % (num, dish, price))

    # Keep asking the user to input a number until a valid one is entered
    while True:
        try:
            e = int(input("\nPlease enter the number of the entrée you'd like to order: "))
            if e not in menu.ordered_Items:
                print("Invalid input. Please enter a number between %d and %d." % (menu.ordered_Items[0], menu.ordered_Items[-1]))
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number between %d and %d." % (menu.ordered_Items[0], menu.ordered_Items[-1]))

    return e


def start_program():
    # print's a welcome message for the user
    print("\nHello Welcome to Sanfords Restaurant"
          "\n\nWhat Can I Serve You Today?"
          "\n\nMenu:")

    # Variables containing lists from the selection's
    main.price = []
    main.order = []
    main.sides = []
    main.sides_Price = []
    main.ordered_Quantity = []

    menu()


def main():
    start_program()

    # Recursive function to keep the program running until the user exits
    def continue_program():
        # Ask the user if they want to continue
        response = input("\nWould you like to order something else? (Y/N): ")

        if response.upper() == "Y":
            menu()
            continue_program()
        elif response.upper() == "N":
            subTotal()
        else:
            print("Invalid input. Please try again.")
            continue_program()

    continue_program()


if __name__ == "__main__":
    main()