budget = float(input())
price_for_1_kg_flour = float(input())
price_for_1_pack_of_eggs = price_for_1_kg_flour * 0.75
price_for_1000_ml_milk = (price_for_1_kg_flour * 0.25) + price_for_1_kg_flour
number_of_loaves = 0
colored_eggs = 0

cost_for_one_loaf = price_for_1_kg_flour + price_for_1_pack_of_eggs + (price_for_1000_ml_milk * 0.25)

while budget > cost_for_one_loaf:
    budget -= cost_for_one_loaf
    number_of_loaves += 1
    colored_eggs += 3
    if number_of_loaves % 3 == 0:
        colored_eggs -= number_of_loaves - 2

print(f'You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')




