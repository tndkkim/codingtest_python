T = int(input())
for _ in range(T):
   result = input()
   score = 0
   combo = 0
   
   for ox in result:
       if ox == 'O':
           combo += 1
           score += combo
       else:
           combo = 0
           
   print(score)