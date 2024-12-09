N = int(input())
P = list(map(int, input().split()))

P.sort()
sum = 0
cnt = len(P)
for i in P:
    sum += cnt*i
    cnt -= 1

print(sum)