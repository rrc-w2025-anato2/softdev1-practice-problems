"""Check if user ID has exactly two digits."""

user_input = input("Enter your user ID: ")

digit_counter = 0
for char in user_input:
    if char.isdigit():
        digit_counter += 1

if digit_counter == 2:
    print("Your user ID is valid.")
else:
    print("Your user ID is invalid.")