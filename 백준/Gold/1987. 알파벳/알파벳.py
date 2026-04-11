import sys
input = sys.stdin.readline

R, C = map(int, input().split())

grids = []
for i in range(R):
    grid = list(input().strip())
    grids.append(grid)

max_dist = 0
visited = set()

def dfs(i, j):
    global max_dist
    max_dist = max(max_dist,len(visited))
    
    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx = i + dx
            ny = j + dy
            
            if 0 <= nx < R and 0 <= ny < C:
                    if grids[nx][ny] not in visited:
                        visited.add(grids[nx][ny])
                        dfs(nx, ny)
                        visited.remove(grids[nx][ny])


visited.add(grids[0][0])
dfs(0,0)
print(max_dist)