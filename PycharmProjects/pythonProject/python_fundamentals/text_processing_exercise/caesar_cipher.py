string = input()
encrypted_string = ''
for character in string:
    encrypted_character = chr(ord(character) + 3)
    encrypted_string += encrypted_character
print(encrypted_string)
