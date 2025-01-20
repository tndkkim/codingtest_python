def prize_2017(a):

    if a == 0: return 0

    if a <= 1: return 5000000

    if a <= 3: return 3000000

    if a <= 6: return 2000000

    if a <= 10: return 500000

    if a <= 15: return 300000

    if a <= 21: return 100000

    return 0

def prize_2018(b):

    if b == 0: return 0

    if b <= 1: return 5120000

    if b <= 3: return 2560000

    if b <= 7: return 1280000

    if b <= 15: return 640000

    if b <= 31: return 320000

    return 0

t = int(input())

for _ in range(t):

    a, b = map(int, input().split())

    print(prize_2017(a) + prize_2018(b))