number = int(input())
students_dict = {}

for i in range(number):
    name = input()
    grade = float(input())

    if name not in students_dict:
        students_dict[name] = []
    students_dict[name].append(grade)
for student in students_dict.keys():
    students_dict[student] = sum(students_dict[student]) / len(students_dict[student])

for student, grade in students_dict.items():
    if grade >= 4.50:
        print(f"{student} -> {grade:.2f}")

