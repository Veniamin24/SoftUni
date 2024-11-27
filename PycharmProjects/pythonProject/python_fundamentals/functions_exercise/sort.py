numbers_as_string = input().split()
numbers_as_integers = []
for number in numbers_as_string:
    numbers_as_integers.append(int(number))

print(sorted(numbers_as_integers))