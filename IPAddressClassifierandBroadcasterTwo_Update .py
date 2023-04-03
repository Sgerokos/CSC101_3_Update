def main():
    # Input validation loop for IP address
    while True:
        ip = input("Please enter a valid IP address: ")
        octets = ip.split(".")

        if is_valid_ip(octets):
            break
        else:
            print("Invalid IP address: It should have four numbers separated by dots, each between 0 and 255.")

    # Determine the class and broadcast status of the IP address
    class_ip = determine_ip_class(octets)
    is_broadcast = is_broadcast_address(octets, class_ip)

    # Print the result
    if is_broadcast:
        print(f"The IP address {ip} is of class {class_ip} and is a broadcast address.")
    else:
        print(f"The IP address {ip} is of class {class_ip} and is not a broadcast address.")


def is_valid_ip(octets):
    if len(octets) != 4:
        return False

    for octet in octets:
        if not octet.isdigit() or int(octet) < 0 or int(octet) > 255:
            return False

    return True


def determine_ip_class(octets):
    first_octet = int(octets[0])

    if 1 <= first_octet <= 126:
        return "A"
    elif 128 <= first_octet <= 191:
        return "B"
    elif 192 <= first_octet <= 223:
        return "C"
    else:
        return "other"


def is_broadcast_address(octets, class_ip):
    if class_ip == "A" and int(octets[1]) == 255 and int(octets[2]) == 255 and int(octets[3]) == 255:
        return True
    elif class_ip == "B" and int(octets[2]) == 255 and int(octets[3]) == 255:
        return True
    elif class_ip == "C" and int(octets[3]) == 255:
        return True
    else:
        return False


if __name__ == '__main__':
    main()