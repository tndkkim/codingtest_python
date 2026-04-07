import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
grid = []
for i in range(N):
    grid.append(list(map(int, input().strip())))

def BFS(graph):
    # visited[x][y][벽을 부쉈는지] = 거리
    visited = [[[-1]*2 for _ in range(M)] for _ in range(N)]
    need_visit = deque()
    
    need_visit.append((0, 0, 0))  # x, y, 벽 부순 횟수
    visited[0][0][0] = 1
    
    while need_visit:
        x, y, k = need_visit.popleft()
        
        if x == N-1 and y == M-1:
            return visited[x][y][k]
        
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0 and visited[nx][ny][k] == -1:
                    visited[nx][ny][k] = visited[x][y][k] + 1
                    need_visit.append((nx, ny, k))
                if graph[nx][ny] == 1 and k == 0 and visited[nx][ny][1] == -1:
                    visited[nx][ny][1] = visited[x][y][k] + 1
                    need_visit.append((nx, ny, 1))
    
    return -1

print(BFS(grid))