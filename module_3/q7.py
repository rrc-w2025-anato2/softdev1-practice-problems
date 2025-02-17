"""Read a single char, check if a valid start char of a variable."""

single_char = input("Enter a character: ")

is_number = single_char.isnumeric()
is_special = not single_char.isalnum()
is_underscore = single_char == "_"

is_valid = is_underscore or (not is_number and not is_special)

if is_valid:
    print("Character is a valid starting character.")
else:
    print("Character is not a valid starting character.")
