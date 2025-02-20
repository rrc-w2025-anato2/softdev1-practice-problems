"""Verify if input is binary and check if it has 3 consecutive ones."""

one_counter = 0

user_input = input("Please enter a binary number: ")

for i in user_input:
    if i not in ("0", "1"):
        print("Input is not in binary format!")
        quit()

print("Accepted" if "111" in user_input else "Rejected")
