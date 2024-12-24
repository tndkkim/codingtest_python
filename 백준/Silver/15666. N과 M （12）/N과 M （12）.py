import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
stack = []

def DFS(start):
    pre = 0
    if len(stack) == M:
        print(*stack)
        return
    for i in range(start, N):
       if numbers[i] != pre:
        pre = numbers[i]
        stack.append(numbers[i])
        DFS(i)
        stack.pop()
DFS(0)