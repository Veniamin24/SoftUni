type = input()
rows = int(input())
cols = int(input())
income = 0
capacity = rows * cols

if type == 'Premiere':
    income = 12 * capacity
elif type == 'Normal':
    income = 7.50 * capacity
elif type == 'Discount':
    income = 5 * capacity

print(f'{income:.2f} leva')