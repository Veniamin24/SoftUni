number_of_groups = int(input())
counter_musala = counter_montblanc = counter_kilimanjaro = counter_k2 = counter_everest = 0
counter_people = 0

for group in range(number_of_groups):
    people_in_group = int(input())
    counter_people += people_in_group

    if people_in_group <= 5:
        counter_musala += people_in_group
    elif 6 <= people_in_group <= 12:
        counter_montblanc += people_in_group
    elif 13 <= people_in_group <= 25:
        counter_kilimanjaro += people_in_group
    elif 26 <= people_in_group <=40:
        counter_k2 += people_in_group
    elif people_in_group > 40:
        counter_everest += people_in_group

print(f'{(counter_musala / counter_people * 100):.2f}%')
print(f'{(counter_montblanc / counter_people * 100):.2f}%')
print(f'{(counter_kilimanjaro / counter_people * 100):.2f}%')
print(f'{(counter_k2 / counter_people * 100):.2f}%')
print(f'{(counter_everest / counter_people * 100):.2f}%')