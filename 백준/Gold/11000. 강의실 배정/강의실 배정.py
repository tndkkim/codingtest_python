import sys
import heapq

input = sys.stdin.readline
N = int(input())

cls = []
for _ in range(N):
    s, t = map(int, input().split())
    cls.append((s, t))
cls.sort(key = lambda x: x[0])

cnt = []
heapq.heappush(cnt, cls[0][1]) #첫번째 강의 종료시간

for i in range(1, N):
    start, end = cls[i]
    if start >= cnt[0]: #강의 끝나는 시간보다 늦게 시작
        heapq.heappop(cnt)
    heapq.heappush(cnt, end)

print(len(cnt))
