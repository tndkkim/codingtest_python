import sys
input = sys.stdin.readline
from collections import deque

# 테스트 케이스 개수 입력
T = int(input())

def BFS(graph, start_node):
    need_visit = deque([start_node])
    
    while need_visit:
        x, y = need_visit.popleft()

        if graph[x][y] == 1:
            graph[x][y] = 0

            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < M and 0 <= ny < N:
                    if graph[nx][ny] == 1:
                        need_visit.append((nx, ny))
    
        

for _ in range(T):
    #M(가로), N(세로), K(배추 개수)
    M, N, K = map(int, input().split())

    #배추 위치 저장
    loc = [[0]*N for _ in range(M)]

    for _ in range(K):
        X, Y = map(int, input().split())
        loc[X][Y] = 1

    sum = 0

    for i in range(M):
        for j in range(N):
            if loc[i][j] == 1:
                BFS(loc, (i, j))
                sum += 1

    print(sum)    
