# Imports the sys package into python
import sys

def subTotal():
    
    # This variable is the tax 8.75%
    sales_Tax = [0.0875]
    
    
    # Variable's used
    # Tax will be calculated by price times sales_Tax
    total = [main.price[i] * main.ordered_Quantity[i] for i in range(len(main.price))]
    tip = [0.10, 0.15, 0.20, 0.25, 0.30]
    tax = [round(main.price[0] * sales_Tax[0], 2)]
    
    total_No_Tax = [round(sum(total))]

    # Total will add price and tax
    total_With_Tax = [round(sum(total + tax), 2)]

    # This is 10% tip, total time's 10%
    ten_Tip = [round(total_With_Tax[0] * tip[0], 2)]

    # This is 15% tip, total time's 15%
    fifteen_Tip = [round(total_With_Tax[0] * tip[1], 2)]

    # This is 20% tip, total time's 20%
    twenty_Tip = [round(total_With_Tax[0] * tip[2], 2)]

    # This is 25% tip, total time's 25%
    twenty_Five_tip = [round(total_With_Tax[0] * tip[3], 2)]      

    # This is 25% tip, total time's 30%
    thirty_Tip = [round(total_With_Tax[0] * tip[4], 2)]                 
    
    # This will print total along with the sale's tax  
    # As well as the recomended tip's and then exit    
    for col_a, col_b, col_c, col_d in zip(main.order, total, main.ordered_Quantity, main.sides):
        print("Order: %s Price: $%0.2f Quantity: %d Side: %s"  
              %(col_a, col_b, col_c, col_d))
    for col_a, col_b, col_c, col_d in zip(total_No_Tax, total_With_Tax, total_No_Tax, tax):
        print("Total Without Tax: $%0.2f Total With Tax: $%0.2f The Total is: $%0.2f Sale's Tax is: $%0.2f" %(col_a, col_b, col_c, col_d))
    
    for col_a, col_b, col_c, col_d, col_e in zip(ten_Tip, fifteen_Tip, twenty_Tip, twenty_Five_tip, thirty_Tip):
        print("Percent Tip is: $%0.2f 15 Percent Tip is: $%0.2f 20 Percent Tip is: $%0.2f 25 Percent Tip is: $%0.2f 30 Percent Tip is: $%0.2f" %(col_a, col_b, col_c, col_d, col_e))

    sys.exit()

def side():

    sides = ["Chicken Orzo Soup", "Field Greens"]
    side_Items = [1, 2]

    # Ask's for a choice in side       
    s = int(input("Do You Want Chicken Orzo Soup or" 
              "\nOrganic Field Greens as a Side"
              "\nPlease Select 1 For Chicken Orzo Soup"
              "\nor 2 For Field Greens: "))
    
    x = side_Items.index(s)
    
    y = sides[x]
    
    main.sides.append(y)    
    
    return main.sides

def yesNo():
    
    
    # This variable will change line 15 look at line 14
    something_Else = input("Would You Like Something Else? \
                          \nPlease Enter Y For Yes or N For No:")

    if something_Else == "Y":
        menu()

    # If N is selected the folowing will be used        
    elif something_Else == "N":
        subTotal()

    # If a anything besides Y or N is selected an error message will be printed  
    elif something_Else != "N" or something_Else != "Y":
        return "Bad Input", userInput()
    
def ordered_Quantity():
    
    amount = int(input("\nHow Many Order's Would You Enjoy: "))  

    main.ordered_Quantity.append(amount)

    return main.ordered_Quantity
         
def confirmation(x):

    # The user will be asked if they want to add this to the order
    y_N = input("Do You Want to Add This to Your order? "
                "\nY For Yes N For No: ")

    # If Y is selected the price will be added to the variable price
    # The order variable will be added to the variable order
    if y_N == "Y":

        i = menu.ordered_Items.index(menu.entrees)
        
        s = menu.menu_Prices[i]
        
        main.price.append(s)

        m = menu.menu_Items[i]

        main.order.append(m)
        
        ordered_Quantity()

        side()

        return main.order, main.price
    # If N is selected no price will be added to the price variable
    # order variable will remain as it did before
    elif y_N == "N":

        menu.order.append("")

        return main.order, main.price

def menu():
    menu.menu_Items = ["Linguini With Stuffed Meatballs - Mozzarella stuffed meatballs, \
cilantro cream sauce.", 
                  "Vegetable Paell - Roasted seasonal vegetables, \
mushrooms, sweet potato, organic red quinoa.", 
                   "Braised Short Rib Cavatell - Baked with mushrooms, \
pearl onions, whipped ricotta", 
                   "Irish Organic Salmon - Flemon cous cous, \
rustic garden vegetables, tomatoes, capers, white wine sauce.",
                   "Teriyaki Chicken - Organic chicken, jasmine rice, \
avocado, stir-fried vegetables", 
                   "Rigatoni With Chicken - Organic chicken, \
house oven dried tomato cream sauce", 
                   "Lobster Ravioli - North atlantic lobster, sherry cream sauce",
                   "Seafood Risotto - Shrimp, calamari, shellfish broth, \
vegetable mire poix.", 
                   "Sesame Crusted Yellowfin Tuna - Shaved brussels sprouts, \
enoki mushrooms, peppers, carrots, soy-ginger broth", 
                   "Blackened Prime Ribeye Steak - Cast iron seared, \
20oz bone in prime ribeye. Sweet potato au gratin."]

    menu.menu_Prices = [26.00, 24.00, 29.00, 29.00, 26.00, 26.00, 
                   32.00, 30.00, 30.00, 52.00]

    menu.ordered_Items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    menu.ordered_Quantity = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


    for col_a, col_b, col_c in zip(menu.ordered_Items, menu.menu_Items, menu.menu_Prices):
        print("%d For: %s Price: $%d"  %(col_a, col_b, col_c))

    menu.entrees = userInput()

    if menu.entrees == 1:
        confirmation(menu.entrees)

    elif menu.entrees == 2:
        confirmation(menu.entrees)

    elif menu.entrees == 3:
        confirmation(menu.entrees)

    elif menu.entrees == 4:
        confirmation(menu.entrees)

    elif menu.entrees == 5:
        confirmation(menu.entrees)

    elif menu.entrees == 6:
        confirmation(menu.entrees)

    elif menu.entrees == 7:
        confirmation(menu.entrees) 

    elif menu.entrees == 8:
        confirmation(menu.entrees)

    elif menu.entrees == 9:
        confirmation(menu.entrees)

    elif menu.entrees == 10:
        confirmation(menu.entrees)

    yesNo()

    return menu.entrees

def userInput():

    # Ask's the user to input a number for one of the items
    e = int(input("\nPlease Select One of The Following Entrées : "))

    return e

def main():

    print("\nHello Welcome to Sanfords Restaurant"
          "\n\nWhat Can I Serve You Today?"
          "\n\nMenu:")

    main.price = []
    main.order = []  
    main.sides = []
    main.ordered_Quantity = []
    count = 1
    m = menu()

    while m != 0:

        m = menu()

        count = count + 1

main()