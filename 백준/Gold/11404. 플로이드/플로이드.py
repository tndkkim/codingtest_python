# import sys
# import heapq 

# input = sys.stdin.readline

# n = int(input()) #도시의 개수
# m = int(input()) #버스의 개수
# group = [[] for _ in range(n+1)]

# for _ in range(m):
#     s, e, w = map(int, input().split())
#     group[s].append((e,w))

# inf = float('inf')

# for start in range(1, n+1):
#     dist = [inf] * (n+1)
#     dist[start] = 0
    
#     pq = [(start, 0)]
#     while pq:
#         node, weight = heapq.heappop(pq)
#         if weight > dist[node] :
#             continue
#         for e, w in group[node]:
#             if dist[node] + w < dist[e]:
#                 dist[e] = dist[node] + w
#                 heapq.heappush(pq, (e, dist[e]))
                
#     print(*[dist[i] for i in range(1, n+1)])


import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

inf = float('inf')

dist = [[inf] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, n+1):
    print(*[0 if dist[i][j] == inf else dist[i][j] for j in range(1, n+1)])