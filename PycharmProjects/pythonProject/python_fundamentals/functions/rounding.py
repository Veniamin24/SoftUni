number_list = input().split()
rounded_values = []

for str_num in number_list:
    rounded_values.append(round(float(str_num)))
print(rounded_values)
