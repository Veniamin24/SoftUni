student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while True:
    movie_name = input()
    if movie_name == 'Finish':
        break
    free_seats = int(input())
    tickets_for_this_movie = 0

    for i in range(free_seats):
        ticket = input()
        if ticket == 'End':
            break
        elif ticket == 'student':
            student_tickets += 1
            tickets_for_this_movie += 1
        elif ticket == 'standard':
            standard_tickets += 1
            tickets_for_this_movie += 1
        elif ticket == 'kid':
            kid_tickets += 1
            tickets_for_this_movie += 1

    print(f'{movie_name} - {((tickets_for_this_movie / free_seats) * 100):.2f}% full.')

total_tickets = standard_tickets + student_tickets + kid_tickets

print(f'Total tickets: {total_tickets}')
print(f'{((student_tickets / total_tickets) * 100):.2f}% student tickets.')
print(f'{((standard_tickets / total_tickets) * 100):.2f}% standard tickets.')
print(f'{((kid_tickets / total_tickets) * 100):.2f}% kids tickets.')