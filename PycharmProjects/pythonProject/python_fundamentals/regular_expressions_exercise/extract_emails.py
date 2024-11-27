import re

some_input = input()
pattern = r'\s([a-z0-9]+[a-z0-9\.\_\-]*@[a-z\-]+(\.[a-z]+)+)\b'
extracted_emails = re.findall(pattern, some_input)

for extracted_email in extracted_emails:
    print(extracted_email[0])
