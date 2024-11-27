from math import floor

number_of_tournaments = int(input())
starting_number_of_points = int(input())
points_from_tournaments = 0
tournaments_won = 0

for tournament in range(number_of_tournaments):
    tournament_finish = input()
    if tournament_finish == 'W':
        points_from_tournaments += 2000
        tournaments_won += 1
    elif tournament_finish == 'F':
        points_from_tournaments += 1200
    elif tournament_finish == 'SF':
        points_from_tournaments += 720

print(f'Final points: {starting_number_of_points + points_from_tournaments}')
print(f'Average points: {floor(points_from_tournaments / number_of_tournaments)}')
print(f'{((tournaments_won / number_of_tournaments) * 100):.2f}%')