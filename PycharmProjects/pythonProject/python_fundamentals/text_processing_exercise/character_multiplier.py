first_string, second_string = input().split()
length = min(len(first_string), len(second_string))
total_sum = 0

for i in range(0, length):
    total_sum += ord(first_string[i]) * ord(second_string[i])
if len(first_string) > len(second_string):
    for i in range(length, len(first_string)):
        total_sum += ord(first_string[i])
else:
    for i in range(length, len(second_string)):
        total_sum += ord(second_string[i])
print(total_sum)

