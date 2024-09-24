hour_start = int(input())
minute_start = int(input())
hour_arrived = int(input())
minute_arrived = int(input())

total_minutes_start = (hour_start * 60) + minute_start
total_minutes_arrived = (hour_arrived * 60) + minute_arrived
total_minutes_difference = total_minutes_start - total_minutes_arrived
hours = abs(total_minutes_difference) // 60
minutes = abs(total_minutes_difference) % 60

if total_minutes_start == total_minutes_arrived:
    print('On time')

elif 0 < total_minutes_start - total_minutes_arrived <= 30:
    print('On time')
    print(f'{total_minutes_start - total_minutes_arrived} minutes before the start')

elif 60 > total_minutes_start - total_minutes_arrived > 30:
    print('Early')
    print(f'{total_minutes_start - total_minutes_arrived} minutes before the start')

elif total_minutes_start - total_minutes_arrived >= 60:
    if minutes < 10:
        print('Early')
        print(f'{hours}:0{minutes} hours before the start')
    else:
        print('Early')
        print(f'{hours}:{minutes} hours before the start')
elif total_minutes_arrived - total_minutes_start < 60:
    print('Late')
    print(f'{total_minutes_arrived - total_minutes_start} minutes after the start')
elif total_minutes_arrived - total_minutes_start >= 60:
    if minutes < 10:
        print('Late')
        print(f'{hours}:0{minutes} hours after the start')
    else:
        print('Late')
        print(f'{hours}:{minutes} hours after the start')