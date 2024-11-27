movie_budget = float(input())
total_spectators = int(input())
spectator_clothes_price = float(input())

movie_decoration = movie_budget * 0.10
if total_spectators > 150:
    spectator_clothes_price -= (spectator_clothes_price * 0.10)

total_amount_needed = movie_decoration + (total_spectators * spectator_clothes_price)

if movie_budget >= total_amount_needed:
    print('Action!')
    print(f'Wingard starts filming with {(movie_budget - total_amount_needed):.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {(total_amount_needed - movie_budget):.2f} leva more.')
