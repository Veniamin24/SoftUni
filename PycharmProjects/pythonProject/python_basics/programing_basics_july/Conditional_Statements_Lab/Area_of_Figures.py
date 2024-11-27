from math import pi

figure = input()
area = 0

if figure == 'square':
    number = float(input())
    area = number * number

elif figure == 'rectangle':
    first_number = float(input())
    second_number = float(input())
    area = first_number * second_number

elif figure == 'circle':
    radius = float(input())
    area = pi * (radius ** 2)

elif figure == 'triangle':
    first_number = float(input())
    second_number = float(input())
    area = 1 / 2 * first_number * second_number

print(f'{area:.3f}')


