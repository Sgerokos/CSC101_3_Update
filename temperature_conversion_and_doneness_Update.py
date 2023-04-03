# Doneness temperatures for Fahrenheit and Celsius
FAHRENHEIT_TEMP = {
    "rare": 120,
    "medium_rare": 130,
    "medium": 140,
    "medium_well": 150,
    "well_done": 160
}

CELSIUS_TEMP = {
    "rare": 49,
    "medium_rare": 55,
    "medium": 60,
    "medium_well": 65,
    "well_done": 70
}

# Fahrenheit option
def fahrenheit_option():
    print("You have selected Fahrenheit")
    f = int(input("Please enter the internal core temperature\nfor Fahrenheit 120-164: "))
    c = (f - 32) / 1.8
    print("The temperature entered is", f, "degrees Fahrenheit and", round(c), "degrees Celsius")
    
    for doneness, temp in FAHRENHEIT_TEMP.items():
        if f < temp:
            print("The meat is", doneness.replace("_", " "), "- Cook for", temp - f, "more degrees for", doneness.title().replace("_", " "))
            break
    
# Celsius option
def celsius_option():
    print("You have selected Celsius")
    c = int(input("Please enter the internal core temperature\nfor Celsius 49-73: "))
    f = (c * 1.8) + 32
    print("The temperature entered is", c, "degrees Celsius and", round(f), "degrees Fahrenheit")
    
    for doneness, temp in CELSIUS_TEMP.items():
        if c < temp:
            print("The meat is", doneness.replace("_", " "), "- Cook for", temp - c, "more degrees for", doneness.title().replace("_", " "))
            break

# Choice function defined
def choice(option):
    if option == 1:
        fahrenheit_option()
    elif option == 2:
        celsius_option()
    else:
        print("Invalid input. Please enter 1 for Fahrenheit or 2 for Celsius.")

# UserInput function defined        
def userInput():
    o = int(input("Welcome to Beef, Veal, and Lamb Internal Temperature Chart:\n"
                  "Fahrenheit and Celsius Cooking Temperatures\n"
                  "Please select 1 for Fahrenheit or 2 for Celsius: "))
    while o < 1 or o > 2:
        print("Error. Please enter a number between 1 and 2.")
        o = int(input("Welcome to Beef, Veal, and Lamb Internal Temperature Chart:\n"
                      "Fahrenheit and Celsius Cooking Temperatures\n"
                      "Please select 1 for Fahrenheit or 2 for Celsius: "))
    return o

# Main function defined
def main():
    option = userInput()
    choice(option)
    
# Call the main function    
main()