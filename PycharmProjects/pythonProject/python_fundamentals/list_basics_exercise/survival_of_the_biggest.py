list_of_integers = input().split()
n = int(input())

numbers_of_integers = []
for number in list_of_integers:
    numbers_of_integers.append(int(number))

for _ in range(n):
    numbers_of_integers.remove(min(numbers_of_integers))
print(*numbers_of_integers, sep=', ')