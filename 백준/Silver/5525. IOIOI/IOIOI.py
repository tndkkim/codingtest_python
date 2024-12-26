n = int(input())
m = int(input())
s = input()

p = 'IO' * n + 'I'
count = 0
pattern = 0
i = 0

while i < m-2:
   if s[i:i+3] == 'IOI':
       pattern += 1
       if pattern == n:
           count += 1
           pattern -= 1
       i += 2
   else:
       pattern = 0
       i += 1

print(count)