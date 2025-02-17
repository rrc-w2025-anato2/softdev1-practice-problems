"""Read 10 integer values and ouput the minimum."""

num_list = []
for i in range(10):
    user_input = int(input("Enter an integer: "))
    num_list.append(user_input)

print(f"The minimum value is {min(num_list)}")
