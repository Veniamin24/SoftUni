people_in_the_jury = int(input())
number_of_presentation = 0
total_assessment_score = 0
while True:
    name_of_presentation = input()
    if name_of_presentation == 'Finish':
        break
    number_of_presentation += 1
    score_per_presentation = 0.0

    for assessment in range(people_in_the_jury):
        score = float(input())
        score_per_presentation += score

    avg_score_per_presentation = score_per_presentation / people_in_the_jury
    total_assessment_score += avg_score_per_presentation
    print(f'{name_of_presentation} - {avg_score_per_presentation:.2f}.')

print(f"Student's final assessment is {(total_assessment_score / number_of_presentation):.2f}.")

