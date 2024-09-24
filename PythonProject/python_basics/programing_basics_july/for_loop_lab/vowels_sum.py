text = input()
result = 0

for i in range(len(text)):
    if text[i] == 'a':
        result += 1
    if text[i] == 'e':
        result += 2
    if text[i] == 'i':
        result += 3
    if text[i] == 'o':
        result += 4
    if text[i] == 'u':
        result += 5

print(result)

