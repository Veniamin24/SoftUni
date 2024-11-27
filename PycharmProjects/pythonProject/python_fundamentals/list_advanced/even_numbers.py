number_list = list(map(int, input().split(', ')))
even_list = []
for number in range(len(number_list)):
    if number_list[number] % 2 == 0:
        even_list.append(number)
print(even_list)
