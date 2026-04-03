import sys
input = sys.stdin.readline

INF = float('inf')

V = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(V):
    nums = list(map(int, input().split()))
    node = nums[0]
    nums.pop(0)
    nums.pop(-1)
    for i in range(0, len(nums), 2):
        v, w = nums[i], nums[i+1]
        graph[node].append((v, w))
        #graph[v].append((node, w)) #양방향 저장
        
#print(*graph)

max_dist = 0
max_node = 0


def dfs(start):
    global max_dist, max_node
    visited = [False] * (V+1)
    stack = [(start, 0)]
    visited[start] = True
    max_dist = 0
    max_node = start
    
    while stack:
        u, d = stack.pop()
        if d > max_dist:
            max_dist = d
            max_node = u
        for a, b in graph[u]:
            if not visited[a]:
                visited[a] = True
                stack.append((a, d+b))
                
                
dfs(1)
u = max_node
dfs(u)
print(max_dist)