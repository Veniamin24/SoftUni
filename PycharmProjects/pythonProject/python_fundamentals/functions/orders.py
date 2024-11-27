def calculate_price(product: str, quantity: int, ):
    if product == 'coffee':
        return quantity * coffee
    elif product == 'coke':
        return quantity * coke
    elif product == 'water':
        return quantity * water
    elif product == 'snacks':
        return quantity * snacks


product = input()
quantity = int(input())
coffee = 1.50
water = 1.00
coke = 1.40
snacks = 2.00
result = calculate_price(product, quantity)
print(f'{result:.2f}')