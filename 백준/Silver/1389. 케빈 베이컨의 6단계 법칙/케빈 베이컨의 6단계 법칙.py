n, m = map(int, input().split())
graph = [[float('inf')]*n for _ in range(n)]

for i in range(n):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

min_value = float('inf')
min_person = 0

for i in range(n):
    sum_value = sum(graph[i])
    if sum_value < min_value:
        min_value = sum_value
        min_person = i+1

print(min_person)