

nylon_needed = int(input())
paint_needed = int(input())
thinner_needed = int(input())
total_hours = int(input())

nylon_cost = 1.50
paint_cost = 14.50
thinner_cost = 5.00
bags = 0.40

total_cost_nylon = (nylon_needed + 2) * 1.50
total_cost_paint = (paint_needed + (paint_needed * 0.10)) * paint_cost
total_cost_thinner = thinner_needed * thinner_cost

total_cost = total_cost_thinner + total_cost_paint + total_cost_nylon + bags
workers_fee = total_cost * 0.30 * total_hours


print(workers_fee + total_cost)