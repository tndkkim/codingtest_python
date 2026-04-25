import sys
input = sys.stdin.readline


def what_level(N):
    total = N*(N+1)//2
    lo, hi = 1, 10**9
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if mid*(mid-1) <= total:
            lo = mid
        else:
            hi = mid - 1
    return lo
    
       
T = int(input())
for _ in range(T):
    
    print(int(what_level(int(input()))))
   
