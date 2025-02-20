"""Verify if input is binary and count the amount of 1s."""

user_input = input("Enter a binary number: ")
is_binary = True
one_count = 0

for i in user_input:
    if i not in ["0", "1"]:
        print("Number is not a valid binary.")
        is_binary = False
        break
    elif i == "1":
        one_count += 1

if is_binary:
    print(f"The number of 1s in the binary: {one_count}")
