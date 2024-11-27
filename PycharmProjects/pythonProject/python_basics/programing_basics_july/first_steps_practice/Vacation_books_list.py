from math import floor


total_pages_in_current_book = int(input())
read_pages_per_hour = int(input())
total_days_per_book = int(input())

print(floor(total_pages_in_current_book / read_pages_per_hour / total_days_per_book))
