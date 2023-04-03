# Set the flag for input validation loop
done = False

# Keep asking for a valid IP address until one is entered
while not done:
    ip = input("Please enter a valid IP address: ")
    lst = ip.split(".")
    
    # Check if the input has four numbers
    if len(lst) != 4:
        print("Invalid IP address: It should have four numbers separated by dots.")
        done = False
    else:
        # Check if each number is within the valid range (0-255)
        for i in lst:
            if not i.isdigit() or int(i) < 0 or int(i) > 255:
                print("Invalid IP address: Each number should be between 0 and 255.")
                done = False
                break
        else:
            # Input is valid, exit the input validation loop
            done = True

# Determine the class of the IP address
if int(lst[0]) <= 126 and int(lst[0]) >= 1:
    classIP = "A"
elif int(lst[0]) <= 191 and int(lst[0]) >= 128:
    classIP = "B"
elif int(lst[0]) <= 223 and int(lst[0]) >= 192:
    classIP = "C"
else:
    classIP = "other"

# Determine if the IP address is a broadcast address
if classIP == "A" and int(lst[1]) == 255 and int(lst[2]) == 255 and int(lst[3]) == 255:
    isBroadcast = True
elif classIP == "B" and int(lst[2]) == 255 and int(lst[3]) == 255:
    isBroadcast = True
elif classIP == "C" and int(lst[3]) == 255:
    isBroadcast = True
else:
    isBroadcast = False

# Print the result
if isBroadcast:
    print(f"The IP address {ip} is of class {classIP} and is a broadcast address.")
else:
    print(f"The IP address {ip} is of class {classIP} and is not a broadcast address.")