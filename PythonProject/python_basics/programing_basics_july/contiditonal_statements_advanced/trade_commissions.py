city = input()
sales_volume = float(input())
commission = 0
ERROR_DATA = False

if city == 'Sofia':
    if 0 <= sales_volume <= 500:
        commission = sales_volume * 0.05
    elif 500 < sales_volume <= 1000:
        commission = sales_volume * 0.07
    elif 1000 < sales_volume <= 10000:
        commission = sales_volume * 0.08
    elif sales_volume > 10000:
        commission = sales_volume * 0.12
    else:
        ERROR_DATA = True

elif city == 'Varna':
    if 0 <= sales_volume <= 500:
        commission = sales_volume * 0.045
    elif 500 < sales_volume <= 1000:
        commission = sales_volume * 0.075
    elif 1000 < sales_volume <= 10000:
        commission = sales_volume * 0.10
    elif sales_volume > 10000:
        commission = sales_volume * 0.13
    else:
        ERROR_DATA = True
elif city == 'Plovdiv':
    if 0 <= sales_volume <= 500:
        commission = sales_volume * 0.055
    elif 500 < sales_volume <= 1000:
        commission = sales_volume * 0.08
    elif 1000 < sales_volume <= 10000:
        commission = sales_volume * 0.12
    elif sales_volume > 10000:
        commission = sales_volume * 0.145
    else:
        ERROR_DATA = True
else:
    ERROR_DATA = True

if ERROR_DATA:
    print('error')
else:
    print(f'{commission:.2f}')
