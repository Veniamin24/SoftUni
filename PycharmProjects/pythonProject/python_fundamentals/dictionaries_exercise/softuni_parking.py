people_registered = {}
number = int(input())

for i in range(number):
    command = input().split()
    if command[0] == 'register':
        name, plate_number = command[1], command[2]
        if name not in people_registered.keys():
            people_registered[name] = plate_number
            print(f"{name} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate_number}")

    elif command[0] == 'unregister':
        name = command[1]
        if name not in people_registered:
            print(f"ERROR: user {name} not found")
        else:
            del people_registered[name]
            print(f"{name} unregistered successfully")
for name, number in people_registered.items():
    print(f'{name} => {number}')



