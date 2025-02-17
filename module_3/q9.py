"""Check if it's an email address."""

email_input = input("Enter an email address: ")

if "@" in email_input:
    print(f"{email_input} is an email address.")
else:
    print(f"{email_input} is NOT an email address.")
