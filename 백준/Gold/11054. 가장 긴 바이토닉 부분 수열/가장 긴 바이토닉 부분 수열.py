n = int(input())
arr = list(map(int, input().split()))

inc = [1] * n
dec = [1] * n

for i in range(n):
   for j in range(i):
       if arr[i] > arr[j]:
           inc[i] = max(inc[i], inc[j] + 1)

for i in range(n-1, -1, -1):
   for j in range(n-1, i, -1):
       if arr[i] > arr[j]:
           dec[i] = max(dec[i], dec[j] + 1)

result = 0
for i in range(n):
   result = max(result, inc[i] + dec[i] - 1)

print(result)