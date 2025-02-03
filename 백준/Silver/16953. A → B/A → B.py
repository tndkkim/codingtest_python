a, b = map(int, input().split())
count = 1
while b > a:
   count += 1
   if b % 2 == 0:
       b //= 2
   elif b % 10 == 1:
       b //= 10
   else:
       break
print(count if b==a else -1)