number_of_people = int(input())
most_points_baker = 0
name_of_the_winner = ''

for i in range(number_of_people):
    total_score_for_baker = 0
    name_of_baker = input()
    while True:
        points_for_the_baker = input()
        if points_for_the_baker == 'Stop':
            break

        points_for_bread = int(points_for_the_baker)
        total_score_for_baker += points_for_bread
    print(f'{name_of_baker} has {total_score_for_baker} points.')
    if total_score_for_baker > most_points_baker:
        most_points_baker = total_score_for_baker
        name_of_the_winner = name_of_baker
        print(f'{name_of_baker} is the new number 1!')

print(f'{name_of_the_winner} won competition with {most_points_baker} points!')


