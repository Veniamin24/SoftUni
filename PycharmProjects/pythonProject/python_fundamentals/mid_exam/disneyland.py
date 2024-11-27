money_needed = int(input())
months = int(input())
saved_money = 0

for month in range(1, months + 1):
    if month % 2 != 0 and month > 1:
        saved_money -= 0.16 * saved_money
    if month % 4 == 0:
        saved_money += 0.25 * saved_money

    saved_money += 0.25 * money_needed

if saved_money >= money_needed:
    print(f'Bravo! You can go to Disneyland and you will have {(saved_money - money_needed):.2f}lv. for souvenirs.')
else:
    print(f'Sorry. You need {(money_needed - saved_money):.2f}lv. more.')
