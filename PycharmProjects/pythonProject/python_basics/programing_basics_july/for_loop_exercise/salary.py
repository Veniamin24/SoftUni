numbers_of_tabs_opened = int(input())
salary = int(input())
flag = True

for tab in range(numbers_of_tabs_opened):
    new_tab = input()
    if new_tab == 'Facebook':
        salary -= 150
    elif new_tab == 'Instagram':
        salary -= 100
    elif new_tab == 'Reddit':
        salary -= 50

    if salary <= 0:
        print('You have lost your salary.')
        flag = False
        break
if flag:
    print(salary)