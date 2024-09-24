import sys
max_number = -sys.maxsize

while True:
    data = input()
    if data == 'Stop':
        break
    number = int(data)
    if number > max_number:
        max_number = number
print(max_number)


