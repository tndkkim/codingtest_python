import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().strip().split())
road = [list(input().strip()) for _ in range(R)]

visited = [[0] * C for _ in range(R)]

jihun = []
fire = []

for i in range (R):
    for j in range(C):
        if road[i][j] == '#':
            visited[i][j] = 1
        elif road[i][j] == 'J':
            jihun.append((i, j))
        elif road[i][j] == 'F':
            fire.append((i, j))


def BFS(road, jihun, fire):
    need_visit = deque(fire + jihun)
    time = 0
    # for row in road:
    #    print(''.join(row))
    while need_visit:
        for _ in range(len(need_visit)):
            x, y = need_visit.popleft()

            if road[x][y] == 'J' and (x == 0 or x == R-1 or y == 0 or y == C-1):
                return time + 1
            
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C:
                    if road[x][y] == 'F' and road[nx][ny] == '.':
                        road[nx][ny] = 'F'
                        need_visit.append((nx, ny))
                    elif road[x][y] == 'J' and road[nx][ny] == '.' and not visited[nx][ny]:
                        road[nx][ny] = 'J'
                        visited[nx][ny] = 1
                        need_visit.append((nx, ny))
            # for row in road:
            #     print(''.join(row))
        time += 1

    return "IMPOSSIBLE"

print(BFS(road, jihun, fire))