import re

pattern = r'(w{3}\.[a-zA-Z0-9-]+(\.[a-z]+)+)'
line = input()
while line:
    match = re.search(pattern, line)
    if match:
        print(match.group(1))
    line = input()

