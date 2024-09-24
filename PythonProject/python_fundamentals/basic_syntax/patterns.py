number = int(input())

for num in range(1, number + 1):
    print('*' * num)
for num in range(number - 1, 0, -1):
    print('*' * num)