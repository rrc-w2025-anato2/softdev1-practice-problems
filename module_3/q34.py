"""Verify if email has only one @ sign."""

user_input = input("Enter an email address: ")

at_counter = 0
for char in user_input:
    if char == "@":
        at_counter += 1

if at_counter == 1:
    print("Email is valid")
else:
    print("Email is invalid")
