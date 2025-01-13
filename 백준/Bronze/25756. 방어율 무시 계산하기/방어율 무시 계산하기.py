n = int(input())
potions = list(map(int, input().split()))

current = 0
for potion in potions:
    p = potion / 100
    current = 1 - (1 - current) * (1 - p)
    print(current * 100)