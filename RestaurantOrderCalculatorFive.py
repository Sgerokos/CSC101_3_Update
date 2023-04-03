# Imports the sys package into python
import sys

def subTotal(price):
        
    # This variable is the tax 8.75%
    sales_Tax = 0.0875
    
    # Variable's used
    # Tax will be calculated by price times sales_Tax
    tax = menu.price * sales_Tax
    
    # Total will add price and tax
    total = menu.price + tax
    
    # This is 10% tip, total time's 10%
    ten_Tip = total * 0.10
    
    # This is 15% tip, total time's 15%
    fifteen_Tip = total * 0.15
    
    # This is 20% tip, total time's 20%
    twenty_Tip = total * 0.20
    
    # This is 25% tip, total time's 25%
    twenty_Five_tip = total * 0.25      
    
    # This is 25% tip, total time's 25%
    thirty_Tip = total * 0.30                  
    
    # This will print total along with the sale's tax  
    # As well as the recomended tip's and then exit
    print("Order's:", menu.order, "\nSide's:", side.sides, 
          "\nTotal Without Tax", menu.price,
          "\nThe Total With Tax is:", round(total, 2),
          "\nThe Total is:", round(total, 2), 
          "\nThe Sale's Tax is:", round(tax, 2), 
          "\n10% Tip is:", round(ten_Tip, 2), 
          "15% Tip is:", round(fifteen_Tip, 2), 
          "20% Tip is:", round(twenty_Tip, 2),
          "25% Tip is:", round(twenty_Five_tip, 2),
          "30% Tip is:", round(thirty_Tip, 2))
    sys.exit()    

def side():
    
    sides = ["Chicken Orzo Soup", "Field Greens"]
    
    side_Items = [1, 2]
    
    side.sides = []
    
    # Ask's for a choice in side       
    s = int(input("Do You Want Chicken Orzo Soup or" 
              "\nOrganic Field Greens as a Side"
              "\nPlease Select 1 For Chicken Orzo Soup"
              "\nor 2 For Field Greens: "))
    
    x = side_Items.index(s)
    
    y = sides[x]
    
    side.sides.append(y)    
    
    return side.sides

def yesNo():

    # This variable will change line 15 look at line 14
    something_Else = input("Would You Like Something Else? \
                          \nPlease Enter Y For Yes or N For No:")

    if something_Else == "Y":
        userInput()
        

    # If N is selected the folowing will be used        
    elif something_Else == "N":
        subTotal(menu.price)
        
    # If a anything besides Y or N is selected an error message will be printed  
    elif something_Else != "N" or something_Else != "Y":
        return "Bad Input", userInput()

def userInput():

    # Ask's the user to input a number for one of the items
    e = int(input("\nHello Welcome to Sanfords Restaurant"
                  "\n\nWhat Can I Serve You Today?"
                  "\n\nMenu:"
                  "\n\n1 For Linguini With Stuffed Meatballs -" 
                  "\nMozzarella stuffed meatballs," 
                  "\ncilantro cream sauce." 
                  "\nPrice: $26"
                  "\n\n2 For Vegetable Paella  -" 
                  "\nRoasted seasonal vegetables, mushrooms,"
                  "\nsweet potato, organic red quinoa," 
                  "\nPrice: $24"
                  "\n\n3 For Braised Short Rib Cavatelli - Baked with mushrooms," 
                  "\npearl onions, whipped ricotta" 
                  "\nPrice: $29"
                  "\n\n4 For Irish Organic Salmon -" 
                  "\nFlemon cous cous, rustic garden vegetables," 
                  "\ntomatoes, capers, white wine sauce." 
                  "\nPrice: $29"
                  "\n\n5 For Teriyaki Chicken - Organic chicken, jasmine rice,"
                  "\navocado, stir-fried vegetables" 
                  "\nPrice: $26"
                  "\n\n6 For Rigatoni With Chicken - Organic chicken," 
                  "\nhouse oven dried tomato cream sauce"
                  "\nPrice: $26"
                  "\n\n7 For Lobster Ravioli  -" 
                  "\nNorth atlantic lobster, sherry cream sauce" 
                  "\nPrice: $32"
                  "\n\n8 For Seafood Risotto - Shrimp, calamari, shellfish broth," 
                  "\nvegetable mire poix."
                  "\nPrice: $30"
                  "\n\n9 For Sesame Crusted Yellowfin Tuna -" 
                  "\nShaved brussels sprouts," 
                  "\nenoki mushrooms, peppers, carrots, soy-ginger broth" 
                  "\nPrice: $30"
                  "\n\n10 For Blackened Prime Ribeye Steak - Cast iron seared," 
                  "\n20oz bone in prime ribeye." 
                  "\nSweet potato au gratin." 
                  "\nPrice: $52"
                  "\n\nPlease Select One of The Following Entrées : "))
    return e
        
def menu(entrees):
    
    menu.menu_Items = ["Linguini With Stuffed Meatballs", "Vegetable Paell", 
               "Braised Short Rib Cavatell", "Irish Organic Salmon",
               "Teriyaki Chicken", "Rigatoni With Chicken", "Lobster Ravioli",
               "Seafood Risotto", "Sesame Crusted Yellowfin Tuna", 
               "Blackened Prime Ribeye Steak"]
    
    menu.menu_Prices = [26.00, 24.00, 29.00, 29.00, 26.00, 26.00, 
                        32.00, 30.00, 30.00, 52.00]
    
    ordered_Items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    ordered_Quantity = []
    
    
    
    # The price is 0 but will be changed as the loop continue's or end's
    #menu_Items.price = []  
    
    # variable order will be set as an empty string till all selections are made
    menu.order = []
    menu.price = 0
    
    
    while entrees != 0:
        
        # If a number not used is selected an error message will be printed out 
        if entrees < 1 or entrees > 10: 
            
            print("\nYou have Inputed an Invalid Number For The Entrées"
                  "\nPlease Enter a number Between 1 - 10 For This Selection")     
    
    
        # Line's 160 - 397 are the selection's that the user will choose from
        # The choice selected will print out what the item is and the price
        elif entrees == 1:
            
            # The user will be asked if they want to add this to the order
            y_N = input("Do You Want to Add This to Your order? "
                        "\nY For Yes N For No: ")
                    
            # If Y is selected the price will be added to the variable price
            # The order variable will be added to the variable order
            if y_N == "Y":
                
                i = ordered_Items.index(entrees)
                                      
                menu.price += menu.menu_Prices[i]
                
                m = menu.menu_Items[i]
                
                menu.order.append(menu.menu_Items[0])
                
                counter = counter + 1
                side()
                
            # If N is selected no price will be added to the price variable
            # order variable will remain as it did before
            elif y_N == "N":
                
                menu.order.append("")
        
        elif entrees == 2:
        
            # The user will be asked if they want to add this to the order
            y_N = input("Do You Want to Add This to Your order? "
                        "\nY For Yes N For No: ")
                    
            # If Y is selected the price will be added to the variable price
            # The order variable will be added to the variable order
            if y_N == "Y":
                
                i = ordered_Items.index(entrees)
                                      
                menu.price += menu.menu_Prices[i]
                
                m = menu.menu_Items[i]
                
                menu.order.append(menu.menu_Items[1])
                
                counter = counter + 1
                
                side()
                
            # If N is selected no price will be added to the price variable
            # order variable will remain as it did before
            elif y_N == "N":
                
                menu.order.append("")
            
        elif entrees == 3:
            
            # The user will be asked if they want to add this to the order
            y_N = input("Do You Want to Add This to Your order? "
                        "\nY For Yes N For No: ")
                    
            # If Y is selected the price will be added to the variable price
            # The order variable will be added to the variable order
            if y_N == "Y":
                
                i = ordered_Items.index(entrees)
                                      
                menu.price += menu.menu_Prices[i]
                
                m = menu.menu_Items[i]
                
                menu.order.append(menu.menu_Items[2])
                
                side()
                
            # If N is selected no price will be added to the price variable
            # order variable will remain as it did before
            elif y_N == "N":
                
                menu.order.append("")
                
        elif entrees == 4:
            
            # The user will be asked if they want to add this to the order
            y_N = input("Do You Want to Add This to Your order? "
                        "\nY For Yes N For No: ")
                    
            # If Y is selected the price will be added to the variable price
            # The order variable will be added to the variable order
            if y_N == "Y":
                
                i = ordered_Items.index(entrees)
                                      
                menu.price += menu.menu_Prices[i]
                
                m = menu.menu_Items[i]
                
                menu.order.append(menu.menu_Items[3])
                
                side()
                
            # If N is selected no price will be added to the price variable
            # order variable will remain as it did before
            elif y_N == "N":
                
                menu.order.append("")
        
        elif entrees == 5:
            
            # The user will be asked if they want to add this to the order
            y_N = input("Do You Want to Add This to Your order? "
                        "\nY For Yes N For No: ")
                    
            # If Y is selected the price will be added to the variable price
            # The order variable will be added to the variable order
            if y_N == "Y":
                
                i = ordered_Items.index(entrees)
                                      
                menu.price += menu.menu_Prices[i]
                
                m = menu.menu_Items[i]
                
                menu.order.append(menu.menu_Items[4])
                
                side()
                
            # If N is selected no price will be added to the price variable
            # order variable will remain as it did before
            elif y_N == "N":
                
                menu.order.append("")         
        
        elif entrees == 6:
            
           # The user will be asked if they want to add this to the order
            y_N = input("Do You Want to Add This to Your order? "
                        "\nY For Yes N For No: ")
                    
            # If Y is selected the price will be added to the variable price
            # The order variable will be added to the variable order
            if y_N == "Y":
                
                i = ordered_Items.index(entrees)
                                      
                menu.price += menu.menu_Prices[i]
                
                m = menu.menu_Items[i]
                
                menu.order.append(menu.menu_Items[5])
                
                side()
                
            # If N is selected no price will be added to the price variable
            # order variable will remain as it did before
            elif y_N == "N":
                
                menu.order.append("")          
        
        elif entrees == 7:
            
            # The user will be asked if they want to add this to the order
            y_N = input("Do You Want to Add This to Your order? "
                        "\nY For Yes N For No: ")
                    
            # If Y is selected the price will be added to the variable price
            # The order variable will be added to the variable order
            if y_N == "Y":
                
                i = ordered_Items.index(entrees)
                                      
                menu.price += menu.menu_Prices[i]
                
                m = menu.menu_Items[i]
                
                menu.order.append(menu.menu_Items[6])
                
                side()
                
            # If N is selected no price will be added to the price variable
            # order variable will remain as it did before
            elif y_N == "N":
                
                menu.order.append("")
                
        elif entrees == 8:
            
            # The user will be asked if they want to add this to the order
            y_N = input("Do You Want to Add This to Your order? "
                        "\nY For Yes N For No: ")
                    
            # If Y is selected the price will be added to the variable price
            # The order variable will be added to the variable order
            if y_N == "Y":
                
                i = ordered_Items.index(entrees)
                                      
                menu.price += menu.menu_Prices[i]
                
                m = menu.menu_Items[i]
                
                menu.order.append(menu.menu_Items[7])
                
                side()
                
            # If N is selected no price will be added to the price variable
            # order variable will remain as it did before
            elif y_N == "N":
                
                menu.order.append("")          
            
        elif entrees == 9:
            
            # The user will be asked if they want to add this to the order
            y_N = input("Do You Want to Add This to Your order? "
                        "\nY For Yes N For No: ")
                    
            # If Y is selected the price will be added to the variable price
            # The order variable will be added to the variable order
            if y_N == "Y":
                
                i = ordered_Items.index(entrees)
                                      
                menu.price += menu.menu_Prices[i]
                
                m = menu.menu_Items[i]
                
                menu.order.append(menu.menu_Items[8])
                
                side()
                
            # If N is selected no price will be added to the price variable
            # order variable will remain as it did before
            elif y_N == "N":
                
                menu.order.append("")
        
        elif entrees == 10:
            
            # The user will be asked if they want to add this to the order
            y_N = input("Do You Want to Add This to Your order? "
                        "\nY For Yes N For No: ")
                    
            # If Y is selected the price will be added to the variable price
            # The order variable will be added to the variable order
            if y_N == "Y":
                
                i = ordered_Items.index(entrees)
                                      
                menu.price += menu.menu_Prices[i]
                
                m = menu.menu_Items[i]
                
                menu.order.append(menu.menu_Items[9])
                
                side()
                
            # If N is selected no price will be added to the price variable
            # order variable will remain as it did before
            elif y_N == "N":
                
                menu.order.append()      

        yesNo()

    return menu.price, menu.order


def main():
    
    main.entrees = userInput()
    
    menu(main.entrees)
    
    subTotal(menu.price)
    
main()