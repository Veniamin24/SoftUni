from math import floor


world_record_seconds = float(input())
distance = float(input())
time_to_pass_one_meter = float(input())

total_time_for_new_record = distance * time_to_pass_one_meter
water_resistance_seconds = floor(distance / 15) * 12.5

final_time = total_time_for_new_record + water_resistance_seconds

if final_time >= world_record_seconds:
    print(f'No, he failed! He was {(final_time - world_record_seconds):.2f} seconds slower.')
else:
    print(f'Yes, he succeeded! The new world record is {final_time:.2f} seconds.')




