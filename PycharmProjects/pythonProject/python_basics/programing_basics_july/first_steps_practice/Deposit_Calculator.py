deposit_amount = float(input())
deposit_period = int(input())
yearly_interest = float(input())

total_amount = deposit_amount + deposit_period * ((deposit_amount * yearly_interest / 100) / 12)
print(total_amount)