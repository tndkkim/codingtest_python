import sys
input = sys.stdin.readline

S = input().strip()
total = []

for i in range(len(S)):
    total.append(S[i:])
total.sort()
print(*total, sep='\n')
