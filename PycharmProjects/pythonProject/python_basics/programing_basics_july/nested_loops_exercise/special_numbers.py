N = int(input())
is_found = False

for number in range(1111, 10000):
    number_to_string = str(number)
    for digit in number_to_string:
        if int(digit) == 0:
            is_found = False
            break
        elif N % int(digit) == 0:
            is_found = True
        else:
            is_found = False
            break
    if is_found:
        print(number, end=" ")