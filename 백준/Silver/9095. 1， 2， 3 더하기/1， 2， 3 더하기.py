def cnt(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return cnt(n-1) + cnt(n-2) + cnt(n-3)

T = int(input())
for _ in range(T):
    n = int(input())
    print(cnt(n))