string_with_names = input().split(', ')
sorted_list = sorted(string_with_names, key=lambda x: (-len(x), x))
print(sorted_list)

