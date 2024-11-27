import re

string = input()
pattern = r'(^|(?<=\s))-*([0]|[1-9][0-9]*)\.*[0-9]*($|(?=\s))'
matches = re.finditer(pattern, string)

for match in matches:
    print(match.group(), end=' ')
