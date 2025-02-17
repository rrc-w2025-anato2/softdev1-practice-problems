"""Read float values from a file named input.txt and display the avg."""

number_list = []
with open("input.txt", "r") as input_file:
    for line in input_file:
        number_list.append(float(line))

print("List of float values from `input.txt`")
print(*number_list, sep=",")
print()

number_list_avg = sum(number_list) / len(number_list)
print(f"List average: {number_list_avg:.2f}")
