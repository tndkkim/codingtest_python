t = int(input())
for _ in range(t):
    n = int(input())
    s = 0
    for k in range(1, n+1):
        s += k * ((k+1)*(k+2)//2)
    print(s)