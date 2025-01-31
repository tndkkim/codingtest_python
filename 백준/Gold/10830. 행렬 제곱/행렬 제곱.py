def multiply_matrix(a, b, n):
   result = [[0]*n for _ in range(n)]
   for i in range(n):
       for j in range(n):
           for k in range(n):
               result[i][j] += a[i][k] * b[k][j]
           result[i][j] %= 1000
   return result

def power(a, b, n):
   if b == 1:
       for i in range(n):
           for j in range(n):
               a[i][j] %= 1000
       return a
   
   temp = power(a, b//2, n)
   if b % 2 == 0:
       return multiply_matrix(temp, temp, n)
   else:
       return multiply_matrix(multiply_matrix(temp, temp, n), a, n)

n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

result = power(matrix, b, n)
for row in result:
   print(*row)