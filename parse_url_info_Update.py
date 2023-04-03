from urllib.parse import urlparse, urlsplit

url = "https://www.serebii.net/pokedex-swsh/"

# Using urlsplit
url_parts = urlsplit(url)
print("URL: ", url_parts.geturl())
print("Scheme: ", url_parts.scheme)
print("Netloc: ", url_parts.netloc)
print("Path: ", url_parts.path)
print("Hostname: ", url_parts.hostname, "(netloc in lower case)")

# Using string slicing
print("\n****************************************************************\n")
print("URL: ", url)
print("Scheme: ", url[0:5])
print("Netloc: ", url[8:23])
print("Path: ", url[23:37])