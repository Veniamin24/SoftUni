looking_for = input()
book_counter = 0
is_found = False

while True:
    new_input = input()
    if new_input == 'No More Books':
        break

    if new_input == looking_for:
        is_found = True
        print(f'You checked {book_counter} books and found it.')
        break

    book_counter += 1
if not is_found:
    print('The book you search is not here!')
    print(f'You checked {book_counter} books.')
