width = int(input())
length = int(input())
height = int(input())

total_cubic_meters = width * length * height

while True:
    new_input = input()
    if new_input == 'Done':
        print(f'{total_cubic_meters} Cubic meters left.')
        break

    total_cubic_meters -= int(new_input)

    if total_cubic_meters <= 0:
        print(f'No more free space! You need {abs(total_cubic_meters)} Cubic meters more.')
        break
