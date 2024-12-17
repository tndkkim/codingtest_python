import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().strip().split())

def BFS(start_node):
    need_visit = deque([start_node])
    visited = [-1] * 100001
    visited[start_node] = 0

    while need_visit:
        crn = need_visit.popleft()

        if crn == K:
            return visited[crn]
        
        for i in [crn-1, crn+1, crn*2]:
            if 0 <= i <= 100000 and visited[i] == -1:
                visited[i] = visited[crn] + 1
                need_visit.append(i)

print(BFS(N))
