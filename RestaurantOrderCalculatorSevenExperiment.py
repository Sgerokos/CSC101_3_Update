def menu_Items(i):
    
    menu_Items.menu_Items = ["Linguini With Stuffed Meatballs", "Vegetable Paell", 
           "Braised Short Rib Cavatell", "Irish Organic Salmon",
           "Teriyaki Chicken", "Rigatoni With Chicken", "Lobster Ravioli",
           "Seafood Risotto", "Sesame Crusted Yellowfin Tuna", 
           "Blackened Prime Ribeye Steak"]
    
    return menu_Items.menu_Items

def menu_Prices(user_Input):

	menu_Prices.menu_Prices = [26.00, 24.00, 29.00, 29.00, 26.00, 26.00, 
	                           32.00, 30.00, 30.00, 52.00]
	
	menu_Prices.menu_Prices = []
	
	return menu_Prices.menu_Prices
def main():
    
   
    
    ordered_Items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    orders = []
    
    user_Input = int(float(input("kjhfasfaj")))
    
    i = ordered_Items.index(user_Input)
                          
    menu_Items(i)
    
    m = menu_Items.menu_Items[i]
    
    
    
    menu_Prices(user_Input)
    

    
    orders.append(m)
    
    print(orders)

main()
                      
