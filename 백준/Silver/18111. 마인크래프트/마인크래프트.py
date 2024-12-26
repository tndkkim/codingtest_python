import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]

min_height = min(min(row) for row in ground)
max_height = max(max(row) for row in ground)

min_time = float('inf')
answer_height = 0

for height in range(min_height, max_height + 1):
    blocks_needed = 0
    blocks_remove = 0
    
    for i in range(n):
        for j in range(m):
            diff = ground[i][j] - height
            if diff > 0:
                blocks_remove += diff
            else:
                blocks_needed -= diff
                
    if blocks_needed <= blocks_remove + b:
        time = blocks_remove * 2 + blocks_needed
        if time <= min_time:
            min_time = time
            answer_height = height

print(min_time, answer_height)