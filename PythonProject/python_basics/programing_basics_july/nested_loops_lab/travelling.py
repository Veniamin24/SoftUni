while True:
    destination = input()
    if destination == 'End':
        break
    budget = float(input())
    savings = 0

    while budget > savings:
        new_input = float(input())
        savings += new_input

    if savings >= budget:
        print(f'Going to {destination}!')






