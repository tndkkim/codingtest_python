from collections import deque
import sys

def bfs(n, k):
    q = deque([n])
    dist = [-1] * 100001
    dist[n] = 0
    
    while q:
        x = q.popleft()
        if x == k:
            return dist[x]
            
        if 2*x <= 100000 and dist[2*x] == -1:
            dist[2*x] = dist[x]
            q.appendleft(2*x)
            
        for nx in (x-1, x+1):
            if 0 <= nx <= 100000 and dist[nx] == -1:
                dist[nx] = dist[x] + 1
                q.append(nx)

n, k = map(int, input().split())
print(bfs(n, k))