"""Enter website names, count the amount of .com."""

user_input = ""
commercial_website_counter = 0

while user_input != "stop":
    user_input = input("Enter a website: ").strip().lower()
    print(user_input[-4:])
    if user_input[-4:] == ".com":
        commercial_website_counter += 1

print(f"Number of commercial websites: {commercial_website_counter}")
