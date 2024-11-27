def calculate_factorial(some_number: int) -> int:
    for multiplier in range(1, some_number):
        some_number *= multiplier
    return some_number


first_num = int(input())
second_num = int(input())
first_factorial = calculate_factorial(first_num)
second_factorial = calculate_factorial(second_num)
result = first_factorial / second_factorial
print(f'{result:.2f}')
