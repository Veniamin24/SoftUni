some_string = input()
final_string = ''
strength = 0
for i in range(len(some_string)):
    if strength > 0 and some_string[i] != '>':
        strength -= 1
    elif some_string[i] == '>':
        final_string += some_string[i]
        strength += int(some_string[i + 1])
    else:
        final_string += some_string[i]
print(final_string)
