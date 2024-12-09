N, K = map(int, input().split())
value = [int(input()) for _ in range(N)]

cnt = 0 #동전 개수
remain = K

for i  in range(N-1, -1, -1):
    if remain >= value[i]:
        cnt += remain//value[i]
        remain %= value[i]
    if remain == 0:
        break
        
print(cnt)