from math import ceil

number_of_days_training = int(input())
km_ran_on_first_day = float(input())

total_km = km_ran_on_first_day

for i in range(1, number_of_days_training + 1):
    new_input = int(input())
    km_ran_on_first_day += (km_ran_on_first_day * new_input) / 100
    total_km += km_ran_on_first_day

if total_km >= 1000:
    print(f"You've done a great job running {ceil(total_km - 1000)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(1000 - total_km)} more kilometers")