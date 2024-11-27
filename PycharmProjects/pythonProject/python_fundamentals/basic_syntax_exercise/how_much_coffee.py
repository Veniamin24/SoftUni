command = input()
coffees = 0

while command != 'END':

    if command == 'dog' or command == 'cat' or command == 'movie' or command == 'coding':
        coffees += 1
    if command == 'DOG' or command == 'CAT' or command == 'MOVIE' or command == 'CODING':
        coffees += 2
    command = input()

if coffees <= 5:
    print(coffees)
else:
    print('You need extra sleep')


