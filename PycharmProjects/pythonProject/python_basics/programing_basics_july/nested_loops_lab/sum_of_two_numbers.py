start_interval = int(input())
final_interval = int(input())
magic_number = int(input())

counter = 0
flag = False

for first_number in range(start_interval, final_interval + 1):
    for second_number in range(start_interval, final_interval + 1):
        counter += 1

        if first_number + second_number == magic_number:
            print(f'Combination N:{counter} ({first_number} + {second_number} = {magic_number})')
            flag = True
            break
    if flag:
        break

if not flag:
    print(f'{counter} combinations - neither equals {magic_number}')