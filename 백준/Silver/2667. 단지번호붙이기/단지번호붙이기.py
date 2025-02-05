n = int(input())
graph = [list(map(int,input())) for _ in range(n)]
result = []

def dfs(x,y):
   if x < 0 or x >= n or y < 0 or y >= n:
       return 0
   
   if graph[x][y] == 1:
       graph[x][y] = 0
       count = 1
       count += dfs(x+1, y)
       count += dfs(x-1, y) 
       count += dfs(x, y+1)
       count += dfs(x, y-1)
       return count
   return 0

for i in range(n):
   for j in range(n):
       if graph[i][j] == 1:
           result.append(dfs(i,j))

print(len(result))
for x in sorted(result):
   print(x)