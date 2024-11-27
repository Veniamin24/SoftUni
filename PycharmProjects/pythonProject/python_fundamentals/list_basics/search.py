n = int(input())
word = input()
string = []

for _ in range(n):
    new_string = input()
    string.append(new_string)

filtered_strings = []
for current_string in string:
    if word in current_string:
        filtered_strings.append(current_string)
print(string)
print(filtered_strings)
