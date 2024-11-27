budget = int(input())
season = input()
total_fishermans = int(input())
boat_rent = 0

if season == 'Spring':
    boat_rent = 3000
elif season == 'Summer' or season == 'Autumn':
    boat_rent = 4200
elif season == 'Winter':
    boat_rent = 2600

if total_fishermans <= 6:
    boat_rent -= (boat_rent * 0.10)
elif 7 < total_fishermans <= 11:
    boat_rent -= (boat_rent * 0.15)
elif total_fishermans > 11:
    boat_rent -= (boat_rent * 0.25)

if total_fishermans % 2 == 0 and season != 'Autumn':
    boat_rent -= (boat_rent * 0.05)

if budget >= boat_rent:
    print(f'Yes! You have {(budget - boat_rent):.2f} leva left.')
else:
    print((f'Not enough money! You need {(boat_rent - budget):.2f} leva.'))