cake_width = int(input())
cake_length = int(input())

total_pieces = cake_length * cake_width

while True:
    new_input = input()
    if new_input == 'STOP':
        print(f'{total_pieces} pieces are left.')
        break

    total_pieces -= int(new_input)

    if total_pieces <= 0:
        print(f'No more cake left! You need {abs(total_pieces)} pieces more.')
        break