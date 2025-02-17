"""Recursive square root of an input till 1.01.

Write a program that prompts the user for a value greater than 10 as an
input (you should loop until the user enters a valid value) and finds
the square root of that number and the square root of the result, and
continues to find the square root of the result until you reach a
number that is smaller than 1.01. The program should output how many
times the square root operation was performed.
"""

from math import sqrt
num_input = 0

while num_input <= 10:
    num_input = input("Enter a number greater than 10: ")
    num_input = int(num_input)

    if num_input <= 10:
        print("Erorr: Please enter a number greater than 10.")

square_root_counter = 0
while num_input >= 1.01:
    display_text = num_input
    num_input = sqrt(num_input)
    print(f"Square root of {display_text:.2f} is {num_input}")

    square_root_counter += 1

print(f"Sqare Root Counter: {square_root_counter}")
