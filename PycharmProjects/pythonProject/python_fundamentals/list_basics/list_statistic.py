n = int(input())

POSITIVE = []
NEGATIVE = []

for _ in range(n):
    number = int(input())

    if number >= 0:
        POSITIVE.append(number)
    else:
        NEGATIVE.append(number)
count_positive_nums =len(POSITIVE)
sum_of_negative_nums = sum(NEGATIVE)

print(POSITIVE)
print(NEGATIVE)
print(f'Count of positives: {count_positive_nums}')
print(f'Sum of negatives: {sum_of_negative_nums}')
