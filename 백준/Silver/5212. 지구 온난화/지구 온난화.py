import sys
input = sys.stdin.readline

grids = []
R, C = map(int, input().split())
for _ in range(R):
    grid = list(input().strip())
    grids.append(grid)
    
result = [row[:] for row in grids]
    
for r in range(R):
    for c in range(C):
        if grids[r][c] == 'X':
            sea = 0
            for dr, dc in [(1,0), (0,1), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c+ dc
                if 0 <= nr < R and 0 <= nc < C:
                    if grids[nr][nc] == '.':
                        sea += 1
                else:
                    sea += 1
            if sea >= 3:
                result[r][c] = '.'

min_r, max_r, min_c, max_c = R, 0, C, 0
for r in range(R):
    for c in range(C):
        if result[r][c] == 'X':
            min_r = min(min_r, r)
            max_r = max(max_r, r)
            min_c = min(min_c, c)
            max_c = max(max_c, c)

for r in range(min_r, max_r + 1):
    print(''.join(result[r][min_c:max_c + 1]))