numbers_as_string = input().split()
numbers_as_integers = []
for number in numbers_as_string:
    numbers_as_integers.append(int(number))
print(f'The minimum number is {min(numbers_as_integers)}')
print(f'The maximum number is {max(numbers_as_integers)}')
print(f'The sum number is: {sum(numbers_as_integers)}')

