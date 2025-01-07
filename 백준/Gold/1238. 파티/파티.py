import heapq
INF = float('inf')

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, time = map(int, input().split())
    graph[start].append((end, time))

def dijkstra(start):
    distances = [INF] * (n+1)
    distances[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    
    while q:
        curr_dist, curr = heapq.heappop(q)
        
        if distances[curr] < curr_dist:
            continue
            
        for next, time in graph[curr]:
            if curr_dist + time < distances[next]:
                distances[next] = curr_dist + time
                heapq.heappush(q, (distances[next], next))
                
    return distances

output = 0
for i in range(1, n+1):
    output = max(output, dijkstra(i)[x] + dijkstra(x)[i])
print(output)