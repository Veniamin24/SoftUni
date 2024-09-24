from math import floor, ceil

price_for_tennis_rocket = float(input())
number_of_tennis_rockets = int(input())
number_of_shoes = int(input())

price_shoes = 1/6 * price_for_tennis_rocket

total_price_for_rockets = price_for_tennis_rocket * number_of_tennis_rockets
total_price_shoes = price_shoes * number_of_shoes

other_equipment = (total_price_for_rockets + total_price_shoes) * 0.20

total_price = total_price_shoes + total_price_for_rockets + other_equipment

price_for_djokovic = total_price / 8
price_for_sponsors = total_price - price_for_djokovic

print(f'Price to be paid by Djokovic {floor(price_for_djokovic)}')
print(f'Price to be paid by sponsors {ceil(price_for_sponsors)}')

