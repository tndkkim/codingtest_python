h, m, s = map(int, input().split())
d = int(input())

total = h * 3600 + m * 60 + s
total += d
total %= 86400
h = total // 3600
m = (total % 3600) // 60
s = total % 60

print(h, m, s)