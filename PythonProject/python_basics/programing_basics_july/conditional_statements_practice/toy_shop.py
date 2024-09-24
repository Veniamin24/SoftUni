price_of_the_trip = float(input())
total_puzzels = int(input())
total_dolls = int(input())
total_bears = int(input())
total_minions = int(input())
total_little_trucks = int(input())

price_puzzels = 2.60
price_dolls = 3
price_bear = 4.10
price_minion = 8.20
price_trucks = 2

total_price = (total_puzzels * price_puzzels) + (total_dolls * price_dolls) + (total_bears * price_bear) + (total_minions * price_minion) + ( total_little_trucks * price_trucks)

if (total_puzzels + total_dolls + total_minions + total_bears + total_little_trucks) >= 50:
    total_price -= (total_price * 0.25)

rent = (total_price * 0.10)

if (total_price - rent) >= price_of_the_trip:
    print(f'Yes! {(total_price - rent - price_of_the_trip):.2f} lv left.')
else:
    print(f'Not enough money! {(price_of_the_trip - (total_price - rent)):.2f} lv needed.')

