# Returns a list of predefined IP addresses
def get_ip_addresses():
    return [
        "74.125.236.145", "209.191.122.70", "207.46.232.182",
        "74.125.236.151", "66.220.149.11", "74.125.236.142", "70.42.185.10",
        "17.149.160.49", "67.228.110.120", "129.42.38.1", "216.239.116.157",
        "64.34.119.12", "137.254.16.101", "138.197.63.241", "72.237.4.113",
        "52.149.246.39", "157.240.229.174", "104.244.42.1", "69.172.200.183"
    ]

# Returns a list of predefined domain names
def get_domains():
    return [
        "google.com", "yahoo.com", "microsoft.com", "gmail.com",
        "facebook.com", "developer.android.com", "pcworld.com",
        "apple.com", "wireshark.org", "ibm.com", "zdnet.com",
        "stackoverflow.com", "oracle.com", "python.org", "utica.edu",
        "duckduckgo.com", "instagram.com", "twitter.com", "pokemon.com"
    ]

# Adds a new IP address and domain name to the respective lists
def add_ip_domain(ip_addresses, domains):
    domain = input("\nPlease enter the domain name you want to add (e.g., example.com): ")
    domains.append(domain)

    ip = input("\nPlease enter the IP address you want to add (e.g., 111.111.1.1): ")
    ip_addresses.append(ip)

    print(domains, ip_addresses)

# Searches and prints the IP address associated with the given domain name
def search_ip_by_domain(ip_addresses, domains):
    domain = input("Please enter the domain name you want to search: ")
    if domain in domains:
        index = domains.index(domain)
        ip = ip_addresses[index]
        print("The domain name is:", domain, "The IP address is:", ip)
    else:
        print("Error: IP not found")

# Searches and prints the domain name associated with the given IP address
def search_domain_by_ip(ip_addresses, domains):
    ip = input("Please enter the IP address you want to search: ")
    if ip in ip_addresses:
        index = ip_addresses.index(ip)
        domain = domains[index]
        print("The IP address is:", ip, "The domain name is:", domain)
    else:
        print("Error: IP not found")


def menu():
    user_input = int(input("\nPlease select one of the following from the menu:"
                           "\n1: Add IP and domain info"
                           "\n2: Look up IP address by domain name"
                           "\n3: Look up domain name by IP address"
                           "\n0: Quit \n"))
    return user_input

# Displays the menu and returns the user's choice
def main():
    ip_addresses = get_ip_addresses()
    domains = get_domains()

    while True:
        user_choice = menu()

        if user_choice == 1:
            add_ip_domain(ip_addresses, domains)
        elif user_choice == 2:
            search_ip_by_domain(ip_addresses, domains)
        elif user_choice == 3:
            search_domain_by_ip(ip_addresses, domains)
        elif user_choice == 0:
            print("Now exiting!!")
            break
        else:
            print("Invalid input. Please try again.")

# Executes the main function when the script is run
if __name__ == "__main__":
    main()