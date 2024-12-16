N, M = map(int, input().split())
numbers = list(map(int, input().split()))

result = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            card_sum = numbers[i] + numbers[j] + numbers[k]
            if card_sum <= M:
                result = max(result, card_sum)

print(result)