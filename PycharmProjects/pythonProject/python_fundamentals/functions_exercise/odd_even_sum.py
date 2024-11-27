def odd_even_sum(number: str) -> str:
    sum_odd_digits = 0
    sum_even_digits = 0
    for digit in number:
        if int(digit) % 2 == 0:
            sum_even_digits += int(digit)
        else:
            sum_odd_digits += int(digit)
    return f"Odd sum = {sum_odd_digits}, Even sum = {sum_even_digits}"


some_number = input()
print(odd_even_sum(some_number))
