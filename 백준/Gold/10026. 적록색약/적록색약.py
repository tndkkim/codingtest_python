from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
visited = [[0] * N for _ in range(N)]
visited2 = [[0] * N for _ in range(N)]


graph = []

for _ in range(N):
    row = list(input().strip())
    graph.append(row)


def bfs(graph, start_node, visited):
    need_visit = deque([start_node])
    x, y = start_node
    color = graph[x][y]
    visited[x][y] = 1

    while need_visit:
        x, y = need_visit.popleft()
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == color and not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    need_visit.append((nx,ny))
                    visited[nx][ny] = 1


def bfs2(graph, start_node, visited):
    need_visit = deque([start_node])
    x, y = start_node
    color = graph[x][y]
    visited[x][y] = 1

    while need_visit:
        x, y = need_visit.popleft()
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny]:
                    if color in ['R', 'G']:
                        if graph[nx][ny] in ['R', 'G']:
                            visited[nx][ny] = visited[x][y] + 1
                            need_visit.append((nx,ny))
                            visited[nx][ny] = 1
                    else:  # color == 'B'
                        if graph[nx][ny] == color:
                            visited[nx][ny] = visited[x][y] + 1
                            need_visit.append((nx,ny))
                            visited[nx][ny] = 1

cnt = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(graph, (i, j), visited)
            cnt += 1

cnt2 = 0
for i in range(N):
    for j in range(N):
        if not visited2[i][j]:
            bfs2(graph, (i, j), visited2)
            cnt2 += 1

print(cnt, cnt2)