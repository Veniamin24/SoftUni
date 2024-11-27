from math import ceil

serial_name = input()
episode_duration = int(input())
rest_duration = int(input())

lunch_time = rest_duration * 0.125
rest_time = rest_duration * 0.25

time_left = rest_duration - lunch_time - rest_time

if time_left >= episode_duration:
    print(f'You have enough time to watch {serial_name} and left with {ceil(time_left - episode_duration)} minutes free time.')
else:
    print(f"You don't have enough time to watch {serial_name}, you need {ceil(episode_duration - time_left)} more minutes." )