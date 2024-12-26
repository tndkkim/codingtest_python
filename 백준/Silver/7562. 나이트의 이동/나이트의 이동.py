from collections import deque

T = int(input())


def BFS(start_node):
    need_visit = deque([start_node])
    visited = [[-1]*l for _ in range(l)]
    visited[start_x][start_y] = 0


    while need_visit:
        x, y = need_visit.popleft()
        
        if x == end_x and y == end_y:
            return visited[x][y]

        for dx, dy in [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < l and 0 <= ny < l and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                need_visit.append((nx, ny))


for _ in range(T):
    l = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    
    print(BFS((start_x, start_y)))