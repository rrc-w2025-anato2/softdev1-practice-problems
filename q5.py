"""Generate three random integers, calculate their avarage.

Generates three random integeres between 0 - 50.
"""

from random import randint

numbers = []
for i in range(3):
    numbers.append(randint(0, 50))

average = sum(numbers) / len(numbers)
print(f"The average of {numbers} is {average:.1f}")
