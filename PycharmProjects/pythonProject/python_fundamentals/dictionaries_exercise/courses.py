data = input().split(' : ')
courses_dict = {}

while 'end' not in data:
    course_name, student = data[0], data[1]
    if course_name not in courses_dict:
        courses_dict[course_name] = []
    courses_dict[course_name].append(student)

    data = input().split(' : ')

for key, value in courses_dict.items():
    print(f'{key}: {len(value)}')
    for name in value:
        print(f'-- {"".join(name)}')
