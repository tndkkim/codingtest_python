from collections import deque

m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

start_node = []
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 1:
                start_node.append((k, i, j))

def BFS(graph, start_node):
    visited = [[[-1]*m for _ in range(n)] for _ in range(h)]
    need_visit = deque()
    
    for z, x, y in start_node:
        need_visit.append((z, x, y))
        visited[z][x][y] = 0
    
    while need_visit:
        z, x, y = need_visit.popleft()
        
        for dz, dx, dy in [(0,1,0), (0,-1,0), (0,0,1), (0,0,-1), (1,0,0), (-1,0,0)]:
            nz = z + dz
            nx = x + dx
            ny = y + dy
            
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
                if graph[nz][nx][ny] == 0 and visited[nz][nx][ny] == -1:
                    visited[nz][nx][ny] = visited[z][x][y] + 1
                    need_visit.append((nz,nx,ny))
                    
    return visited

output = BFS(graph, start_node)

max_day = 0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 0 and output[k][i][j] == -1:
                print(-1)
                exit(0)
            max_day = max(max_day, output[k][i][j])

print(max_day)