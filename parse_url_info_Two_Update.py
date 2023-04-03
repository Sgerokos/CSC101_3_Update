# Defines a function path
def path (url):

    path = url[url.rfind (".") + 4:]

    return path

# Defines a function netloc
def netloc (url):

    domain = url[url.rfind("www"):url.rfind(".") + 4]

    return domain

# Defines a function scheme
def scheme(url):

    scheme = url[:url.rfind("://")]

    return scheme

# Defines a function main
def main():
    
    # Variable that stores the url
    url = input("Please Enter The Absolute URL: \n")
    # Un # this line and # the previous 
    # to place the url inside the program instead of typing it
    # url = "https://www.utica.edu/directory/computer-science-department"
    # url = ("https://www.serebii.net/pokedex-swsh/")
    
    path(url)
    netloc(url)
    scheme(url)

    # Print's the information by spliting the string
    print("\n****************************************************************\n"
          "URL Info: \n"
          "\n- URL:", url,
          "\n- Scheme:", scheme(url),
          "\n- Netloc (Domain):", netloc(url),
          "\n- Path:", path(url),
          "\n\n****************************************************************")
    
# Call's the main function
main()