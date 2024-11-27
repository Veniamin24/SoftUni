users_points_dict = {}
courses_dict = {}
while True:
    result = input().split('-')
    if len(result) == 1:
        break
    elif len(result) == 2:
        banned_name = result[0]
        del users_points_dict[banned_name]
    else:
        name, course, points = result[0], result[1], int(result[2])
        if name not in users_points_dict:
            users_points_dict[name] = 0
        if points > users_points_dict[name]:
            users_points_dict[name] = points
        if course not in courses_dict.keys():
            courses_dict[course] = 0
        courses_dict[course] += 1
print('Results:')
for name, points in users_points_dict.items():
    print(f'{name} | {points}')
print('Submissions:')
for language, submissions in courses_dict.items():
    print(f'{language} - {submissions}')
