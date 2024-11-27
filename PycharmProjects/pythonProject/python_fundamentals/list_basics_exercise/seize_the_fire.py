fires_with_cells = input().split('#')
water = int(input())
effort = 0
total_fire = 0
list_with_cells = []

for fire_cell in fires_with_cells:
    current_cell = fire_cell.split(' = ')
    type_of_fire = current_cell[0]
    value_of_cell = int(current_cell[1])
    if water < value_of_cell:
        continue
    if type_of_fire == 'High' and 81 <= value_of_cell <= 125:
        water -= value_of_cell
        effort += value_of_cell * 0.25
        total_fire += value_of_cell
        list_with_cells.append(f'{value_of_cell}')
    elif type_of_fire == 'Medium' and 51 <= value_of_cell <= 80:
        water -= value_of_cell
        effort += value_of_cell * 0.25
        total_fire += value_of_cell
        list_with_cells.append(f'{value_of_cell}')
    elif type_of_fire == 'Low' and 1 <= value_of_cell <= 50:
        water -= value_of_cell
        effort += value_of_cell * 0.25
        total_fire += value_of_cell
        list_with_cells.append(f'{value_of_cell}')

print('Cells:')

for value_of_cell in list_with_cells:
    print(f' - {value_of_cell}')

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')

