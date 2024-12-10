import sys
from collections import Counter

N = int(sys.stdin.readline())
num = []
for _ in range(N):
    num.append(int(sys.stdin.readline()))
    
count = Counter(num)
item = list(count.items())
#print(item)

item.sort(key=lambda x: (-x[1], x[0]))
print(item[0][0])