num1 = int(input())
num2 = int(input())

for num in range(num1, num2 + 1):
    sum_even = 0
    sum_odd = 0
    for idx, digit in enumerate(str(num)):
        if idx % 2 == 0:
            sum_even += int(digit)

        elif idx % 2 != 0:
            sum_odd += int(digit)

    if sum_odd == sum_even:
        print(num, end=' ')

