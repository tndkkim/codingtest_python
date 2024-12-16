import sys
input = sys.stdin.readline

N = int(input())
score = [int(input()) for _ in range(N)]
ans = 0
for i in range(N-1, 0, -1):
    tmp = 0
    while score[i] <= score[i-1]:
        score[i-1] -= 1
        tmp += 1
    ans += tmp
print(ans)