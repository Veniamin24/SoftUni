list_of_numbers = [int(number) for number in input().split()]

command = input().split()
while 'END' not in command:
    action = command[0]
    if action == 'Change':
        painting_number = int(command[1])
        new_number = int(command[2])
        if painting_number in list_of_numbers:
            index = list_of_numbers.index(painting_number)
            list_of_numbers.remove(painting_number)
            list_of_numbers.insert(index, new_number)

    elif action == 'Hide':
        painting_number = int(command[1])
        if painting_number in list_of_numbers:
            list_of_numbers.remove(painting_number)

    elif action == 'Switch':
        painting_number1 = int(command[1])
        painting_number2 = int(command[2])
        if painting_number1 in list_of_numbers and painting_number2 in list_of_numbers:
            first_position = list_of_numbers.index(painting_number1)
            second_position = list_of_numbers.index(painting_number2)
            list_of_numbers[first_position], list_of_numbers[second_position] =\
                list_of_numbers[second_position], list_of_numbers[first_position]

    elif action == 'Insert':
        index = int(command[1])
        painting_number = int(command[2])
        if index + 1 in range(len(list_of_numbers)):
            list_of_numbers.insert(index + 1, painting_number)

    if action == 'Reverse':
        list_of_numbers.reverse()

    command = input().split()
print(' '.join(str(number) for number in list_of_numbers))


