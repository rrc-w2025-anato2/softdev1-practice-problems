"""Match user ID and a password."""

USER_ID = "admin"
USER_PW = "open"

input_id = input("Enter your user ID: ")
input_pw = input("Enter your password: ")

if input_id == USER_ID and input_pw == USER_PW:
    print("Welcome")
elif input_id != USER_ID and input_pw != USER_PW:
    print("Sorry, wrong ID and password")
elif input_id == USER_ID:
    print("Wrong password")
else:
    print("Wrong user ID")
