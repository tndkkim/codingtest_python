import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 4 2
numbers = sorted(list(map(int, input().split()))) # 9 7 9 1 -> 1 7 9 9
stack = []
visited = [0] * N

def DFS():
    pre = 0
    if len(stack) == M:
        print(*stack)
        return
    for i in range(N):
        if not visited[i] and numbers[i] != pre:
            visited[i] = 1
            pre = numbers[i]
            stack.append(numbers[i])
            DFS()
            visited[i] = 0
            stack.pop()
DFS()