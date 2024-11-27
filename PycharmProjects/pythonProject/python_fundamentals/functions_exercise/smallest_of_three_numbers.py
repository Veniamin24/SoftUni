# def smallest_number(num1, num2, num3):
#     return min(num1, num2, num3)
#
#
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# print(smallest_number(num1, num2, num3))

def smallest(list_with_numbers: list) -> int:
    return min(list_with_numbers)

first_number = int(input())
second_number = int(input())
third_number = int(input())
print(smallest([first_number, second_number, third_number]))
