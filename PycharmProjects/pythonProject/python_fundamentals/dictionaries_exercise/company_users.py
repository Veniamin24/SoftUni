data = input().split(' -> ')
dictionary = {}

while 'End' not in data:
    company, employee = data[0], data[1]
    if company not in dictionary:
        dictionary[company] = []
    if employee not in dictionary[company]:
        dictionary[company].append(employee)
    data = input().split(' -> ')

for key, value in dictionary.items():
    print(f'{key}')
    for i in value:
        print(f'-- {"".join(i)}')