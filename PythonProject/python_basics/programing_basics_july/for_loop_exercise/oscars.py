name = input()
points = float(input())
numbers_of_evaluators = int(input())
is_points_enough = False

for evaluator in range(numbers_of_evaluators):
    new_evaluator = input()
    given_points = float(input())
    points += ((len(new_evaluator) * given_points) / 2)

    if points >= 1250.5:
        print(f'Congratulations, {name} got a nominee for leading role with {points:.1f}!')
        is_points_enough = True
        break

if not is_points_enough:
    print(f'Sorry, {name} you need {(1250.5 - points):.1f} more!')