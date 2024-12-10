import sys
N = int(sys.stdin.readline())
result = [0] * N

for i in range(N):
    result[i] = int(sys.stdin.readline())
result.sort()
print(*result, sep='\n')