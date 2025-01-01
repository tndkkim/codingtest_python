from collections import deque

n, m = map(int, input().split())
campus = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
count = 0

for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            start_x, start_y = i, j
            break

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque([(start_x, start_y)])
visited[start_x][start_y] = True

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and campus[nx][ny] != 'X':
            visited[nx][ny] = True
            if campus[nx][ny] == 'P':
                count += 1
            q.append((nx, ny))

print('TT' if count == 0 else count)