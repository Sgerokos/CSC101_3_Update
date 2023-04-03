def main():
    # Welcome message and user input for temperature unit
    option = int(input("Welcome to Beef, Veal, and Lamb"
                       "\nInternal Temperature Chart:"
                       "\nFahrenheit and Celsius Cooking Temperatures"
                       "\nPlease Select 1 For Fahrenheit or 2 For Celsius: "))

    if option == 1:
        process_fahrenheit()
    elif option == 2:
        process_celsius()
    else:
        print("The Input You Have Entered is Not Recognized."
              "\nPlease Input 1 For Fahrenheit or 2 For Celsius."
              "\nThank You!!!")


def process_fahrenheit():
    print("You Have Selected Fahrenheit")
    f = int(input("Please Enter The Internal Core Temperature"
                  "\nFor Fahrenheit 120-164: "))

    # Calculate Celsius
    c = (f - 32) / 1.8

    # Determine doneness and display information
    display_doneness(f, c, True)


def process_celsius():
    print("You Have Selected Celsius")
    c = int(input("Please Enter The Internal Core Temperature"
                  "\nFor Celsius 49-73: "))

    # Calculate Fahrenheit
    f = (c * 1.8) + 32

    # Determine doneness and display information
    display_doneness(c, f, False)


def display_doneness(temp1, temp2, is_fahrenheit):
    doneness_ranges = [
        ("Rare", (120, 125), (49, 51),
         "Center is bright red, pinkish toward the exterior portion, and warm throughout."),
        ("Medium Rare", (130, 135), (55, 57),
         "Center is very pink, slightly brown toward the exterior portion, and slightly hot."),
        ("Medium", (140, 145), (60, 63),
         "Center is light pink, outer portion is brown, and hot throughout."),
        ("Medium Well", (150, 155), (65, 69),
         "Mostly gray-brown throughout with a hint of pink in the center."),
        ("Well Done", (160, 164), (70, 73),
         "Mostly gray-brown throughout with a hint of pink in the center.")
    ]

    temp_ranges = [item[1] if is_fahrenheit else item[2] for item in doneness_ranges]

    for i, (doneness, f_range, c_range, description) in enumerate(doneness_ranges):
        if temp_ranges[i][0] <= temp1 <= temp_ranges[i][1]:
            print(f"The Meat is {doneness} - {description}")
            print(f"The Temperature Entered is {temp1} Degrees {'Fahrenheit' if is_fahrenheit else 'Celsius'}")
            print(f"And {round(temp2)} Degrees {'Celsius' if is_fahrenheit else 'Fahrenheit'}")

            for j in range(i + 1, len(temp_ranges)):
                degrees_to_next_doneness = temp_ranges[j][0] - temp1
                next_doneness = doneness_ranges[j][0]
                print(f"Cook for {degrees_to_next_doneness} more degrees for {next_doneness}")

            break
    else:
        print("The Input You Have Entered is Not Recognized."
              f"\nPlease Input a Number Ranging From {temp_ranges[0][0]}-{temp_ranges[-1][1]}."
              "\nThank You!!!")


if __name__ == '__main__':
    main()