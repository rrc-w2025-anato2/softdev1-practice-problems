"""Take 10 exam grades bet. 0-100, output the min, max and avg."""

min_value = 0
max_value = 0
avg_value = 0

input_counter = 1
exam_grades = []

while input_counter <= 10:
    user_input = int(input("Enter an exam grade: "))
    if user_input < 0 or user_input > 100:
        print("Enter an exam grade between 0 and 100.")
        continue
    exam_grades.append(user_input)
    input_counter += 1

min_value = min(exam_grades)
max_value = max(exam_grades)
avg_value = sum(exam_grades) / len(exam_grades)

print(f"Min value: {min_value}, Max value: {max_value}, Avg value: {avg_value}")