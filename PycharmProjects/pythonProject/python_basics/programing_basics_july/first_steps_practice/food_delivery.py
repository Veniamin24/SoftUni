total_chicken_menus = int(input())
total_fish_menus = int(input())
total_vegetarian_menus = int(input())

total_price_for_chicken_menus = total_chicken_menus * 10.35
total_price_for_fish_menus = total_fish_menus * 12.40
total_price_for_vegetarian_menus = total_vegetarian_menus * 8.15

total_price = total_price_for_chicken_menus + total_price_for_vegetarian_menus + total_price_for_fish_menus
desert_price = total_price * 0.20
total_cost = total_price + desert_price + 2.50


print(total_cost)
