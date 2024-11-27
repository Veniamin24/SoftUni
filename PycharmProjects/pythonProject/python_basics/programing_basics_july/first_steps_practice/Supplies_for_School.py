pencils = int(input())
markers = int(input())
detergent = int(input())
discount = int(input())

one_pack_of_pens_price = 5.80
one_pack_of_marks_price = 7.20
detergent_per_litre = 1.20

total_cost_pens = pencils * one_pack_of_pens_price
total_cost_marks = markers * one_pack_of_marks_price
total_cost_detergent = detergent * detergent_per_litre

total_cost = total_cost_pens + total_cost_marks + total_cost_detergent
total_cost_with_discount = total_cost - (total_cost * discount / 100)

print(total_cost_with_discount)