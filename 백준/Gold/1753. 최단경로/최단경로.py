import sys
import heapq

input = sys.stdin.readline



INF = float('inf')
V, E = map(int, input().split()) #5 6
K = int(input())# 1 (시작점)
graph = [[] for _ in range(V+1)] # [] [] [] [] [] [], graph[0]은 안씀 그냥 정점 번호(1~V)랑 인덱스 맞추기 위한 V+1


for _ in range(E):
    u, v, w = map(int, input().split())#5 1 1 / 1 2 2/ 1 3 3 / 2 3 4 / 2 4 5 / 3 4 6
    graph[u].append((v, w))

#print(*graph) #[] [(2, 2), (3, 3)] [(3, 4), (4, 5)] [(4, 6)] [] [(1, 1)]
#무방향 그래프였으면 graph[v]에도 추가 필요

dist = [INF] * (V + 1) #초기 거리 : INF(무한)설정 -> 거리를 못찾으면 그대로 출력
dist[K] = 0 #출발점 거리가중치 0
pq = [(0, K)] #우선순위큐, (거리, 정점) 형태 저장, 시작점k/거리0 시작

while pq: #우선순위큐가 빌 떄까지
    d, u = heapq.heappop(pq) #큐에서 거리가 가장 작은 (d, u) pop
    if d > dist[u]: #d가 이미 저장된 최소거리보다 길면 pass
        continue
    for v, w in graph[u]:
        if dist[u] + w < dist[v]: #u의 이웃 정점 v확인, 짧으면 거리 갱신
            dist[v] = dist[u] + w
            heapq.heappush(pq, (dist[v], v)) #큐에 (d, v)추가
            
for i in range(1, V+1):
    print(dist[i] if dist[i] != INF else "INF")


# root = [0] * V
# for i in range(E):
#     if edges[i][0] == (K+i):
#         dir = edges[i][1]
#         dir += root[i-1] if root[i-1] != 0 else 0
#         if root[i] == 0:
#             root[i] = dir
#         elif dir < root[i]:
#             root[i] = dir
            
# print(*root)
    
    
    
    