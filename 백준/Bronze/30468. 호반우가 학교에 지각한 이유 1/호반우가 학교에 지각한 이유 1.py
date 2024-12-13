STR, DEX, INT, LUK, N = map(int, input().split())

current_sum = STR + DEX + INT + LUK
target_sum = N * 4

if current_sum >= target_sum:
    print(0)
else:
    print(target_sum - current_sum)