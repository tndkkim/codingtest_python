import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
X= list(map(int,sys.stdin.readline().split())) # 2 4 -10 4 -9
tmp = sorted(list(set(X)))

for i in X:
    print(bisect_left(tmp, i), end=' ')
