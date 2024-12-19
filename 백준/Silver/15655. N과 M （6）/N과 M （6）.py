import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
stack = []

def DFS(start):
    if len(stack) == M:
        print(*stack)
        return
        
    for i in range(start, N):
        stack.append(numbers[i])
        DFS(i + 1)
        stack.pop()

DFS(0)