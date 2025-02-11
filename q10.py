"""Validate user password match."""

register_msg = "You are now a registered user."
typo_msg = "Sorry, there's a typo in your message."

first_password = input("Enter your password: ")
second_password = input("Enter the same password again: ")

print(register_msg if first_password == second_password else typo_msg)
