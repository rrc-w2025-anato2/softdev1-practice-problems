"""Generate two random numbers between 0 and 100."""

from random import randint

a, b = [randint(0, 100), randint(0, 100)]
print(a if a < b else b)
