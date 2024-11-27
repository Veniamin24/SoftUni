string = input()
for index in range(len(string)):
    if string[index] == ':':
        if index + 1 in range(len(string)):
            print(f'{string[index]}{string[index + 1]}')
