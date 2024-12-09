N = int(input())
weight = [int(input()) for _ in range(N)]

weight.sort(reverse=True)
max = 0
for i in range(N):
    if (i+1)*weight[i] >= max:
        max = (i+1)*weight[i]
print(max)