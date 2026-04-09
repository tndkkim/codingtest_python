import sys
input = sys.stdin.readline

N, M = map(int, input().split())

player = [[] for _ in range(N)]
score = [0] * N
for i in range(N):
    card = list(map(int, input().split()))
    card.sort(reverse=True)
    player[i] = card

for i in range(M):
    max_card = 0 
    for j in range(N):
        if max_card < player[j][0]:
            max_card = player[j][0]
    for j in range(N):
        if player[j][0] == max_card:
            score[j] += 1
        player[j].pop(0)

winner = [i + 1 for i, v in enumerate(score) if v == max(score)]
print(*winner)
        
        