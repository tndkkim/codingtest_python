import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
answer = 0
for k in range(20):
    count = 0
    for a in A:
        if a & (1 << k): # k번 비트가 1인 원소
            count += 1
    answer = max(answer, count)
    
print(answer)