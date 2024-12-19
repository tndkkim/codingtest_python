import sys
input = sys.stdin.readline

N = int(input())
stack = []
cnt = 0
visited = [[0] * N for _ in range(N)]

def DFS(row):
    global cnt
    if row == N:
        cnt += 1
        return

    for col in range(N):
        if visited[row][col] == 0:
            stack.append((row, col))
            queen(row, col, 1)
            DFS(row+1)
            stack.pop()
            queen(row, col, -1)

def queen(row, col, num):

    for i in range(N):
        visited[i][col] += num

    r, c = row, col
    while r >= 0 and c >= 0:
        visited[r][c] += num
        r -= 1
        c -= 1
    
    r, c = row, col
    while r >= 0 and c < N:
        visited[r][c] += num
        r -= 1
        c += 1

    r, c = row, col
    while r < N and c < N:
        visited[r][c] += num
        r += 1
        c += 1
    
    r, c = row, col
    while r < N and c >= 0:
        visited[r][c] += num
        r += 1
        c -= 1

DFS(0)
print(cnt)
