length = int(input())
width = int(input())
height = int(input())
percents = float(input())

volume_aquarium = length * width * height
volume_litres = volume_aquarium / 1000
litres_needed = volume_litres * (1 - (percents / 100))
print(litres_needed)
