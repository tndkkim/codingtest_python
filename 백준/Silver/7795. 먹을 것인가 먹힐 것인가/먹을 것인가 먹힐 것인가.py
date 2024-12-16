import sys
from bisect import bisect_left
input = sys.stdin.readline

T = int(input())
        
for _ in range(T):
    N, M = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))

    B.sort()

    sum = 0
    for i in A:
        sum += bisect_left(B, i)
    print(sum)
    