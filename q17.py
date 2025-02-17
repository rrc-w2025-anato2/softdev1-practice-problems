"""Print if input contains @ character."""

user_input = ""

while "@" not in user_input:
    user_input = input("Enter a word containing the @ character: ")
    if "@" in user_input:
        print("Word has the '@' character!")
        print(user_input)
