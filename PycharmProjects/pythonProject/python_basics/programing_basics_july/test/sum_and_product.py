n = int(input())
flag = False

for a in range(1, 10):
    for b in range(9, a, -1):
        for c in range(10):
            for d in range(9, c, -1):
                if a + b + c + d == a * b * c * d and n % 10 == 5:
                    print(f'{a}{b}{c}{d}')
                    flag = True
                    break
                elif (a * b * c * d) // (a + b + c + d) == 3 and n % 3 == 0:
                    print(f'{d}{c}{b}{a}')
                    flag = True
                    break

            if flag:
                break
if not flag:
    print('Nothing found')