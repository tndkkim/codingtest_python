from collections import deque
import sys
input = sys.stdin.readline

def bfs(a, b):
    q = deque([(a, "")])
    visited = set([a])
    
    while q:
        num, path = q.popleft()
        if num == b:
            return path
            
        next_num = (num * 2) % 10000
        if next_num not in visited:
            visited.add(next_num)
            q.append((next_num, path + 'D'))
            
        next_num = (num - 1) if num else 9999
        if next_num not in visited:
            visited.add(next_num)
            q.append((next_num, path + 'S'))
            
        next_num = (num % 1000) * 10 + num // 1000
        if next_num not in visited:
            visited.add(next_num)
            q.append((next_num, path + 'L'))
            
        next_num = (num % 10) * 1000 + num // 10
        if next_num not in visited:
            visited.add(next_num)
            q.append((next_num, path + 'R'))

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(bfs(a, b))