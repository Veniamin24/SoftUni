wanted_money_for_the_day = int(input())
money_counter = 0
flag = False

while wanted_money_for_the_day > money_counter:
    service = input()
    if service == 'closed':
        flag = True
        break
    if service == 'haircut':
        kind_of_service = input()
        if kind_of_service == 'mens':
            money_counter += 15
        elif kind_of_service == 'ladies':
            money_counter += 20
        elif kind_of_service == 'kids':
            money_counter += 10
    elif service == 'color':
        kind_of_service = input()
        if kind_of_service == 'touch up':
            money_counter += 20
        elif kind_of_service == 'full color':
            money_counter += 30

if flag:
    print(f'Target not reached! You need {wanted_money_for_the_day - money_counter}lv. more.')
    print(f'Earned money: {money_counter}lv.')
else:
    print(f'You have reached your target for the day!')
    print(f'Earned money: {money_counter}lv.')

