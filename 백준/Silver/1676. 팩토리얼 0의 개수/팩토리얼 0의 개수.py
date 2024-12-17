import math

n = int(input())
result = math.factorial(n)

total = 0
str_result = str(result)

for digit in str_result[::-1]:
   if digit == '0':
       total += 1
   else:
       break

print(total)