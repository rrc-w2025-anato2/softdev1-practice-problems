"""Validate user ID if it's between 6-10 chars in length."""

user_id = input("Enter your user ID")
if len(user_id) >= 6 and len(user_id) <= 10:
    print(f"Welcome, {user_id}")
else:
    print("Sorry, user ID is invalid.")
