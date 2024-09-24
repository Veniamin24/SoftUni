number_of_paper = int(input())
number_of_matter = int(input())
liters_of_glue = float(input())
discount = int(input())

paper_price = 5.80
matter_price = 7.20
glue_price = 1.20

total_cost_paper = paper_price * number_of_paper
total_cost_matter = matter_price * number_of_matter
total_cost_glue = glue_price * liters_of_glue

total_cost = total_cost_matter + total_cost_glue + total_cost_paper

total_cost -= (total_cost * discount) / 100

print(f'{total_cost:.3f}')
