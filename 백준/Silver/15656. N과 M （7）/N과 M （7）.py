import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
stack = []

def DFS():
    if len(stack) == M:
        print(*stack)
        return
    for i in range(N):
        stack.append(numbers[i])
        DFS()
        stack.pop()
DFS()