from itertools import combinations

N, M = map(int, input().split())
houses = []
chickens = []

for r in range(N):
    row = list(map(int, input().split()))
    for c in range(N):
        if row[c] == 1:
            houses.append((r, c))
        elif row[c] == 2:
            chickens.append((r, c))

ans = float('inf')

for selected in combinations(chickens, M):
    total = 0
    for h in houses:
        min_dist = min(abs(h[0]-c[0]) + abs(h[1]-c[1]) for c in selected)
        total += min_dist
    ans = min(ans, total)

print(ans)