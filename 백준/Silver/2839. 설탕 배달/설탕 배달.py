N = int(input())
cnt = 0
find = False
for i in range(max(N//5, N//3), -1, -1):
    temp = N - 5*i
    if temp%3 == 0 and temp>=0:
        cnt += i + temp//3
        print(cnt)
        find = True
        break

if not find: print(-1)