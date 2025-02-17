"""Output 'Hello World' nth times."""

user_input = ""
while True:
    try:
        user_input = int(input("Please enter a positive integer: "))
        if user_input <= 0:
            raise ValueError()
        break
    except ValueError:
        print("Please enter a positive integer, try again!")

for i in range(user_input):
    print("Hello World")
