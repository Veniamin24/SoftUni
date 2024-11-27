list_with_numbers = input().split(' ')
opposite_numbers = []

for num in list_with_numbers:
    opposite_number = -int(num)
    opposite_numbers.append(opposite_number)
print(opposite_numbers)
