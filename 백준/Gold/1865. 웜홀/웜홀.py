import sys
input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    N, M, W = map(int, input().split())
    
    edges = []
    
    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))
    
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))
    
    dist = [0] * (N + 1)
    flag = False

    for i in range(N):
        for S, E, T in edges:
            if dist[S] + T < dist[E]:
                dist[E] = dist[S] + T
                if i == N - 1:
                    flag = True
    
    print("YES" if flag else "NO")