team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

game_terminated = False
players = input().split()
for player in players:
    team, number = player.split('-')
    if int(number) in team_a and team == 'A':
        team_a.remove(int(number))
    elif int(number) in team_b and team == 'B':
        team_b.remove(int(number))
    if len(team_a) < 7 or len(team_b) < 7:
        game_terminated = True
        break
print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
if game_terminated:
    print('Game was terminated')