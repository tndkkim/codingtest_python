import sys
import heapq

input = sys.stdin.readline
N = int(input())

line = []
for _ in range(N):
    x, y = map(int, input().split())
    line.append((x, y))
line.sort(key = lambda x: x[0])

ans = 0
end = line[0][1]
start = line[0][0]

for x, y in line[1:]:
    if x <= end:
        end = max(end, y)
    else:
        ans += end -start
        start = x
        end = y

ans += end - start
print(ans)