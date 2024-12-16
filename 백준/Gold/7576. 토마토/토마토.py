from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

start_node = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            start_node.append((i, j))

def BFS(graph, start_node):
    visited = [[-1] * m for _ in range(n)]
    need_visit = deque()

    for x, y in start_node:
        need_visit.append((x, y))
        visited[x][y] = 0
   
    while need_visit:
        x, y = need_visit.popleft()

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    need_visit.append((nx,ny))

    return visited

output = BFS(graph, start_node)

max_day = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and output[i][j] == -1:
            print(-1)
            exit(0)
        max_day = max(max_day, output[i][j])

print(max_day)