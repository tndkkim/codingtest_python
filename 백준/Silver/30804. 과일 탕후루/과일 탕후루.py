n = int(input())
s = list(map(int, input().split()))

max_len = 0
start = 0
count = {}

for end in range(n):
   count[s[end]] = count.get(s[end], 0) + 1
   
   while len(count) > 2:
       count[s[start]] -= 1
       if count[s[start]] == 0:
           del count[s[start]]
       start += 1
   
   max_len = max(max_len, end - start + 1)

print(max_len)