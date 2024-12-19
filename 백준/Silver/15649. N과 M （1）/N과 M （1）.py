import sys
input = sys.stdin.readline

N, M = map(int, input().split())
stack = []
visited = [0] * (N+1)

def DFS():
    if len(stack) == M:
        print(*stack)
        return
    for i in range(1, N+1):
        if not visited[i]:
            stack.append(i)
            visited[i] = 1
            DFS()
            visited[i] = 0
            stack.pop()
DFS()