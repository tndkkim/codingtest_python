a, b, c = map(int, input().split())

if c == 0:
    print(int((a + b) ** 0.5))
elif b == 0:
    print(c * c - a)
else:
    print(c * c - b)