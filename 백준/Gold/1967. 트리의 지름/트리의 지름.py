import sys
input = sys.stdin.readline

INF = float('inf')

n = int(input()) #노드의 개수
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    p, c, w = list(map(int, input().split()))
    graph[p].append((c, w))
    graph[c].append((p, w))
        
#print(*graph)

max_dist = 0
max_node = 0
def dfs(start):
    global max_dist, max_node
    visited = [False] * (n+1)
    stack = [(start, 0)]
    visited[start] = True
    max_dist = 0
    max_node = start
    
    while stack:
        c, w = stack.pop()
        if w > max_dist:
            max_dist = w
            max_node = c
        for a, b in graph[c]:
            if not visited[a]:
                visited[a] = True
                stack.append((a, w+b))
                
                
dfs(1)
dfs(max_node)
print(max_dist)