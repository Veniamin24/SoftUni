tax_for_year = int(input())

shoes = tax_for_year - (tax_for_year * 0.40)
jersey = shoes - (shoes * 0.20)
ball = jersey * 1/4
accessories =  ball * 1/5

total_cost = tax_for_year + shoes + jersey + ball + accessories
print(total_cost)