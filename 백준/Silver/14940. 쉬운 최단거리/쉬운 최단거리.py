from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1]*m for _ in range(n)]

start = None
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start = (i, j)
            dist[i][j] = 0
        elif graph[i][j] == 0:
            dist[i][j] = 0

need_visit = deque([start])
while need_visit:
    x, y = need_visit.popleft()
    for dx, dy in [(1,0), (-1, 0), (0, 1), (0, -1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                need_visit.append((nx, ny))

for i in dist:
    print(*i)