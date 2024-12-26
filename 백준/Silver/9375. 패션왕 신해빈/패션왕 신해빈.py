from collections import defaultdict

t = int(input())
for _ in range(t):
   n = int(input())
   clothes = defaultdict(int)
   
   for _ in range(n):
       name, type = input().split()
       clothes[type] += 1
   
   result = 1
   for count in clothes.values():
       result *= (count + 1)
       
   print(result - 1)