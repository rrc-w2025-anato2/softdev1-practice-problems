"""Read a web address and output its domain."""

web_domains = {
    "gov": "govenrment",
    "edu": "university",
    "com": "business",
    "org": "organization"
}

web_address = input("Enter a web address: ")
domain = web_address.split(".")[-1]
if domain in web_domains:
    print(f"It is a {web_domains[domain]} web address.")
