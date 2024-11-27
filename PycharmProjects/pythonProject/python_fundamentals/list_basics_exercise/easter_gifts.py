gifts = input().split()
command = input()

while not command == "No Money":
    command = command.split()
    if "OutOfStock" in command:
        for current_gift in range(len(gifts)):
            if command[1] in gifts[current_gift]:
                gifts[current_gift] = "None"
    elif "Required" in command:
        for current_gift in range(len(gifts)):
            if current_gift == int(command[2]):
                gifts[current_gift] = command[1]
    elif "JustInCase" in command:
        gifts[-1] = command[1]
    command = input()
while "None" in gifts:
    gifts.remove("None")
print(*gifts)




