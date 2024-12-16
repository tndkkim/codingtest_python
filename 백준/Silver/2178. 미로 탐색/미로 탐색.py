from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

def BFS(graph, start_node):
    visited = [[0] * m for _ in range(n)]
    need_visit = deque([start_node])
    x, y = start_node
    visited[x][y] = 1 
    
    while need_visit:
        node = need_visit.popleft()
        x, y = node
        
        if x == n-1 and y == m-1:
            return visited[x][y]
            
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    need_visit.append((nx,ny))
    return 0

def DFS(graph, start_node):
    visited = [[0] * m for _ in range(n)]
    need_visit = [start_node]
    visited[0][0] = 1

    while need_visit:
        x, y = need_visit.pop()

        if x== n-1 and y == m-1:
            return visited[x][y]
        for dx, dy in [(1, 0), (-1,0), (0,1), (0,-1)]:
            nx = x + dx
            ny =  y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    need_visit.append((nx, ny))
    return visited[n-1][m-1]

#print(DFS(graph, (0, 0)))


print(BFS(graph, (0,0)))