flower_type = input()
total_flowers = int(input())
budget = int(input())
total_amount = 0

if flower_type == 'Roses':
    total_amount = 5 * total_flowers
    if total_flowers > 80:
        total_amount -= (total_amount * 0.10)
elif flower_type == 'Dahlias':
    total_amount = 3.80 * total_flowers
    if total_flowers > 90:
        total_amount -= (total_amount * 0.15)
elif flower_type == 'Tulips':
    total_amount = 2.80 * total_flowers
    if total_flowers > 80:
        total_amount -= (total_amount * 0.15)
elif flower_type == 'Narcissus':
    total_amount = 3 * total_flowers
    if total_flowers < 120:
        total_amount += (total_amount * 0.15)
elif flower_type == 'Gladiolus':
    total_amount = 2.50 * total_flowers
    if total_flowers < 80:
        total_amount += (total_amount * 0.20)

if budget >= total_amount:
    print(f'Hey, you have a great garden with {total_flowers} {flower_type} and {(budget - total_amount):.2f} leva left.')
else:
    print(f'Not enough money, you need {(total_amount - budget):.2f} leva more.')