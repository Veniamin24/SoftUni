name = input()
grades_total = 0
years_counter = 0
failed_counter = 0

while years_counter < 12:
    annual_grade = float(input())

    if annual_grade < 4:
        failed_counter += 1
        if failed_counter == 2:
            print(f'{name} has been excluded at {years_counter + 1} grade')
            break
        continue

    years_counter += 1
    grades_total += annual_grade

else:
    average_grade = grades_total / 12
    print(f'{name} graduated. Average grade: {average_grade:.2f}')

