"""Generate five random integers between 60 to 100, print the lowest."""

from random import randint

numbers = []
for i in range(0, 5):
    numbers.append(randint(60, 100))

numbers.sort()
print(numbers[0])
