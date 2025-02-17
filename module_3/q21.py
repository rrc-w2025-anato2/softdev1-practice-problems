"""Count multiple of 7 between 33 and 97."""

counter = 0
for i in range(33, 98):
    if i % 7 == 0:
        counter += 1
        # print(i)

print(f"Number of seven multiples: {counter}")
