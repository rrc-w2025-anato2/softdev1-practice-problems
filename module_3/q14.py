"""Read a string representing a year."""

year_input = input("Enter a year: ")

if len(year_input) == 2:
    print(2000 + int(year_input))
elif len(year_input) == 4:
    print(int(year_input))
else:
    print("The year is invalid.")
