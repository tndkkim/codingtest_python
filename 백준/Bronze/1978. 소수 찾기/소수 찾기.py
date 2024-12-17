import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().strip().split()))

cnt = [1] * N

for i in range(N):
   if num[i] == 1:
       cnt[i] = 0
   else:
       for j in range(2, num[i]):
           if num[i] % j == 0:  
               cnt[i] = 0
               break

print(sum(cnt))