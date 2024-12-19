import sys
input = sys.stdin.readline

N, M = map(int, input().split())
stack = []

def DFS():
    if len(stack) == M:
        print(*stack)
        return
    for i in range(1, N+1):
        stack.append(i)
        DFS()
        stack.pop()
DFS()