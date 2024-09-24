days = int(input())
type_of_room = input()
rating = input()
price = 0


room_for_one_person = 18
apartment = 25
president_apartment = 35

nights = days - 1

if type_of_room == 'room for one person':
    price = nights * room_for_one_person

elif type_of_room == 'apartment':
    price = nights * apartment
    if nights < 10:
        price -= price * 0.30
    elif 10 <= nights <= 15:
        price -= price * 0.35
    elif nights > 15:
        price -= price * 0.50

elif type_of_room == 'president apartment':
    price = nights * president_apartment
    if nights < 10:
        price -= price * 0.10
    elif 10 <= nights <= 15:
        price -= price * 0.15
    elif nights > 15:
        price -= price * 0.20

if rating == 'positive':
    price += price * 0.25
elif rating == 'negative':
    price -= price * 0.10

print(f'{price:.2f}')






