dictionary_quantity = {}
dictionary_price = {}
command = input().split()

while 'buy' not in command:
    name, price, quantity = command[0], float(command[1]), int(command[2])
    if name not in dictionary_quantity.keys():
        dictionary_quantity[name] = 0
        dictionary_price[name] = 0.00
    dictionary_quantity[name] += quantity
    dictionary_price[name] = price
    command = input().split()

for key, value in dictionary_quantity.items():
    price = value * dictionary_price[key]
    print(f'{key} -> {price:.2f}')



