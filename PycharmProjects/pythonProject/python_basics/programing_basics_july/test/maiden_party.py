money_needed_for_party = float(input())
number_love_messages = int(input())
number_of_roses = int(input())
number_of_keychain = int(input())
number_of_caricature = int(input())
number_of_lucky_surprise = int(input())

love_message = 0.60
rose = 7.20
keychain = 3.60
caricature = 18.20
lucky_surprise = 22

total_price = (number_of_caricature * caricature) + (number_of_roses * rose) + \
(number_of_keychain * keychain) + (number_of_lucky_surprise * lucky_surprise) + (number_love_messages * love_message)

item_counter = number_of_lucky_surprise + number_of_roses + number_of_caricature + \
number_of_keychain + number_love_messages

if item_counter >= 25:
    total_price -= total_price * 0.35

total_price -= total_price * 0.10

if total_price >= money_needed_for_party:
    print(f'Yes! {(total_price - money_needed_for_party):.2f} lv left.')
else:
    print(f'Not enough money! {(money_needed_for_party - total_price):.2f} lv needed.')