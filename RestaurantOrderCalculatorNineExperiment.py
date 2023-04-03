menu_Items = ["Linguini With Stuffed Meatballs", "Vegetable Paell", 
               "Braised Short Rib Cavatell", "Irish Organic Salmon",
               "Teriyaki Chicken", "Rigatoni With Chicken", "Lobster Ravioli",
               "Seafood Risotto", "Sesame Crusted Yellowfin Tuna", 
               "Blackened Prime Ribeye Steak"]
menu_Prices = [26.00, 24.00, 29.00, 29.00, 26.00, 26.00, 
                        32.00, 30.00, 30.00, 52.00]
    
ordered_Items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
ordered_Quantity = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

order = []*10

price = 0
count = 0
while count < 100:
    entrees = int(input("jaskfns:"))
    i = ordered_Items.index(entrees)
    price += menu_Prices[i]
                    
    m = menu_Items[i]
                    
    order.append(m)
    count = count+1
    print(order)