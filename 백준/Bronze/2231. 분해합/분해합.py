N = input()
max_sum = len(N)
N = int(N)
found = False

#각 자리 수의 합 : 9*자리수 <- 이게 최대
min = max(0, N - (9 * max_sum))
for i in range(min, N):
    a = i + sum(map(int, str(i)))
    if a == N:
        print(i)
        found = True
        break
if not found:
    print(0)