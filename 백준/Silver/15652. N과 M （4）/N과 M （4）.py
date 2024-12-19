import sys
input = sys.stdin.readline

N, M = map(int, input().split())
stack = []

def DFS(start):
    if len(stack) == M:
        print(*stack)
        return
        
    for i in range(start, N+1):
        stack.append(i)
        DFS(i)
        stack.pop()

DFS(1)