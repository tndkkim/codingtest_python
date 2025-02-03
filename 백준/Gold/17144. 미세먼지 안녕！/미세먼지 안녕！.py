r, c, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(r)]

cleaner = []
for i in range(r):
   if grid[i][0] == -1:
       cleaner.append(i)

def spread():
   dx = [-1, 1, 0, 0]
   dy = [0, 0, -1, 1]
   temp = [[0]*c for _ in range(r)]
   
   for x in range(r):
       for y in range(c):
           if grid[x][y] <= 0:
               continue
           spread_value = grid[x][y] // 5
           spread_count = 0
           for i in range(4):
               nx = x + dx[i]
               ny = y + dy[i]
               if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] != -1:
                   temp[nx][ny] += spread_value
                   spread_count += 1
           grid[x][y] -= spread_value * spread_count
   
   for i in range(r):
       for j in range(c):
           grid[i][j] += temp[i][j]

def clean_air():
   top = cleaner[0]
   for i in range(top-1, 0, -1):
       grid[i][0] = grid[i-1][0]
   for i in range(c-1):
       grid[0][i] = grid[0][i+1]
   for i in range(top):
       grid[i][c-1] = grid[i+1][c-1]
   for i in range(c-1, 1, -1):
       grid[top][i] = grid[top][i-1]
   grid[top][1] = 0
   
   bottom = cleaner[1]
   for i in range(bottom+1, r-1):
       grid[i][0] = grid[i+1][0]
   for i in range(c-1):
       grid[r-1][i] = grid[r-1][i+1]
   for i in range(r-1, bottom, -1):
       grid[i][c-1] = grid[i-1][c-1]
   for i in range(c-1, 1, -1):
       grid[bottom][i] = grid[bottom][i-1]
   grid[bottom][1] = 0

for _ in range(t):
   spread()
   clean_air()

result = sum(sum(row) for row in grid) + 2
print(result)