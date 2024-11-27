goal = 10000
steps_walked = 0

while steps_walked < goal:
    command = input()
    if command != 'Going home':
        steps_walked += int(command)
    else:
        steps_walked += int(input())
        break

if steps_walked >= goal:
    print(f'Goal reached! Good job!')
    print(f'{steps_walked - goal} steps over the goal!')
else:
    print(f'{goal - steps_walked} more steps to reach goal.')