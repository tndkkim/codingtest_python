import sys
input = sys.stdin.readline
N = list(map(int, input().split()))

sum = 0
for i in range(len(N)):
    sum += N[i]**2
    
print(sum%10)
