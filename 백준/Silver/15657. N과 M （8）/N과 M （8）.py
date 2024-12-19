import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
stack = []
visited = [0] * N

def DFS(start):
    if len(stack) == M:
        print(*stack)
        return
    for i in range(start, N):
        stack.append(numbers[i])
        DFS(i)
        stack.pop()
DFS(0)