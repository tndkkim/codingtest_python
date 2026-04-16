import sys
input = sys.stdin.readline

def maxd(n):
    k = (n + 1) // 2
    if n % 2 == 1:
        return k * k
    else:
        return k * k + k

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    d = y - x
    n = 1
    while not (n <= d <= maxd(n)):
        n += 1
    print(n)