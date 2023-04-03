def is_valid_ipv4_address(ipv4):
    # Check if each number in the IPv4 address is within the valid range
    for x in ipv4:
        num = int(x)
        if num < 0 or num > 255 or (x[0] == "0" and len(x) > 1):
            return False
    return True

def is_valid_ipv6_address(ipv6):
    # Check if each group in the IPv6 address has a valid length and characters
    for group in ipv6:
        if len(group) > 4:
            return False

        for char in group:
            if not (char.isdigit() or 'A' <= char <= 'F' or 'a' <= char <= 'f'):
                return False
    return True

def validate_ip_address(ip):
    ipv4 = ip.split(".")
    ipv6 = ip.split(":")

    if len(ipv4) == 4 and is_valid_ipv4_address(ipv4):
        return ip, "is a valid IPv4 IP address"
    elif len(ipv6) == 8 and is_valid_ipv6_address(ipv6):
        return ip, "is a valid IPv6 IP address"
    else:
        return ip, "is neither IPv4 nor IPv6"

def main():
    while True:
        ip = input("\nPlease enter a valid IP address:\n")
        print("\nIP Address:", *validate_ip_address(ip))

main()