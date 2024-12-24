import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = sorted(list(map(int, input().split())))

cnt = 0
stack = []

def DFS(start):
    global cnt
    for i in range(start, N):
        stack.append(nums[i])
        if sum(stack) == S:
            cnt += 1

        DFS(i+1)
        stack.pop()

DFS(0)
print(cnt)