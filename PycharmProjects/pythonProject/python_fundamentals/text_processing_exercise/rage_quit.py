some_string = input()
rage_message = ''
sub_string = ''
repetitions = ''
for index in range(len(some_string)):
    if not some_string[index].isdigit():
        sub_string += some_string[index].upper()
    else:
        for next_digits in range(index, len(some_string)):
            if not some_string[next_digits].isdigit():
                break
            repetitions += some_string[next_digits]
        rage_message += sub_string * int(repetitions)
        sub_string = ''
        repetitions = ''
print(f'Unique symbols used: {len(set(rage_message))}')
print(rage_message)