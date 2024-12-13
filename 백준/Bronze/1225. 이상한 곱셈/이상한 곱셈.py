A, B = input().split()

total = 0
for i in range(10):
   a_count = str(A).count(str(i))
   for j in range(10):
       b_count = str(B).count(str(j))
       total += i * j * a_count * b_count

print(total)