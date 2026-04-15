import sys
input = sys.stdin.readline

# 연료 행렬 저장
grids = []
N, M = map(int, input().split())
for _ in range(N):
    grid = list(map(int, input().split()))
    grids.append(grid)

#dp로 grids[n][m]까지의 최소연료양 계산
INF = float('inf')
dp = [[[INF]*3 for _ in range(M)] for _ in range(N)]
for m in range(M):
    for d in range(3):
        dp[0][m][d] = grids[0][m]

for n in range(N):
    for m in range(M):
        for d in range(3):
            if dp[n][m][d] == INF:
                continue
            for nd, (dn, dm) in enumerate([(1,-1),(1,0),(1,1)]):
                if nd == d:  #같은 방향으로 연속으로 음직일 수 없음
                    continue
                nn, nm = n+dn, m+dm
                if 0 <= nn < N and 0 <= nm < M:
                    dp[nn][nm][nd] = min(dp[nn][nm][nd], dp[n][m][d] + grids[nn][nm])

print(min(dp[N-1][m][d] for m in range(M) for d in range(3))) #달에서 연료가 가장 최소인 지점 출력