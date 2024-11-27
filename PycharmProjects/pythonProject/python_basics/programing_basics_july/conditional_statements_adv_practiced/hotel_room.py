month = input()
total_nights = int(input())
price_studio = 0.0
price_apartment = 0.0

if month == 'May' or month == 'October':
    price_studio = 50
    price_apartment = 65
    if 7 < total_nights <= 14:
        price_studio -= price_studio * 0.05
    elif total_nights > 14:
        price_studio -= price_studio * 0.30

if month == 'June' or month == 'September':
    price_studio = 75.20
    price_apartment = 68.70
    if total_nights > 14:
        price_studio -= price_studio * 0.20

if month == 'July' or month == 'August':
    price_studio = 76
    price_apartment = 77

total_amount_studio = total_nights * price_studio
total_amount_apartment = total_nights * price_apartment

if total_nights > 14:
    total_amount_apartment -= total_amount_apartment * 0.10

print(f'Apartment: {total_amount_apartment:.2f} lv.')
print(f'Studio: {total_amount_studio:.2f} lv.')

