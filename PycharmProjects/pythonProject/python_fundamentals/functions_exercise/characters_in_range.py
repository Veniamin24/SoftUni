def characters_between(first, second):
    all_characters = []
    for current_character in range(ord(first) + 1, ord(second)):
        all_characters.append(chr(current_character))
    return all_characters


first_char = input()
second_char = input()
result = characters_between(first_char, second_char)
print(' '.join(result))
