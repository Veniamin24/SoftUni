def sum_numbers(first_num, second_num):
    return first_num + second_num


def subtract(result, third_num):
    return result - third_num


def add_and_subtract(first, second , third):
    sum_result = sum_numbers(first, second)
    final_result = subtract(sum_result, third)
    return final_result


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))
