t = int(input())

for _ in range(t):
   y, m = map(int, input().split())
   d = m
   r = m
   
   while r >= d:
       r -= d
       m -= 1
       if m < 1:
           m = 12
           y -= 1
       if m in [4,6,9,11]:
           d = 30
       elif m == 2:
           d = 29 if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0 else 28
       else:
           d = 31
           
   print(y, m, d-r)