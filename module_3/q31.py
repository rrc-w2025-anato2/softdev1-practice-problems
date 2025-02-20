"""Dow Jones Average for 7 days."""

from sys import float_info

with open("dja.txt", "r") as dja_file:
    dja_numbers = dja_file.readlines()
    if len(dja_numbers) == 0:
        print("File is empty")
    else:
        # Convert from str to float
        dja_numbers = list(map(float, dja_numbers))
        # Only get lines 1-7
        dja_numbers = dja_numbers[:7]

        min_value = float_info.max()
        min_value = min(dja_numbers)
        min_value_idx = dja_numbers.index(min_value)
        print(f"The minimum value is {min_value} at day {min_value_idx + 1}")
