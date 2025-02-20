"""Verify if input is binary and check if it has at exactly two ones."""

one_counter = 0
is_binary = False

user_input = input("Please enter a binary number: ")

for i in user_input:
    if i not in ("0", "1"):
        print("Input is not in binary format!")
        quit()

print("Accepted" if user_input == "11" else "Rejected")
