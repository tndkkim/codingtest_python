t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    x -= 1
    y -= 1
    k = x
    found = False
    
    while k < m * n:
        if k % n == y:
            print(k + 1)
            found = True
            break
        k += m
            
    if not found:
        print(-1)