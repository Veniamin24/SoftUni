hour = int(input())
minutes = int(input())

new_minutes = minutes + 15

if (new_minutes - 60) >= 0:
    hour += 1
    new_minutes -= 60
if hour > 23:
    hour = 0

if new_minutes < 10:
    print(f'{hour}:0{new_minutes}')
else:
    print(f'{hour}:{new_minutes}')
