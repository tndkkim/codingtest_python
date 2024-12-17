N, M = map(int, input().split())
board = [input() for _ in range(N)]
min_count = 64

for i in range(N-7):
    for j in range(M-7):
        count1 = 0  #흰
        count2 = 0  #검
        
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x + y) % 2 == 0:
                    if board[x][y] != 'W':
                        count1 += 1
                    if board[x][y] != 'B':
                        count2 += 1
                else:
                    if board[x][y] != 'B':
                        count1 += 1
                    if board[x][y] != 'W':
                        count2 += 1
        
        min_count = min(min_count, count1, count2)

print(min_count)