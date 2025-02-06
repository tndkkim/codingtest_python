from collections import deque

n, m = map(int, input().split())
board = [0] * 101
visited = [False] * 101

for _ in range(n):
   x, y = map(int, input().split())
   board[x] = y

for _ in range(m):
   u, v = map(int, input().split())
   board[u] = v

def bfs():
   q = deque([(1, 0)])
   visited[1] = True
   
   while q:
       pos, cnt = q.popleft()
       if pos == 100:
           return cnt
           
       for i in range(1, 7):
           next_pos = pos + i
           if next_pos > 100 or visited[next_pos]:
               continue
               
           if board[next_pos] != 0:
               next_pos = board[next_pos]
           
           if not visited[next_pos]:
               visited[next_pos] = True
               q.append((next_pos, cnt + 1))

print(bfs())