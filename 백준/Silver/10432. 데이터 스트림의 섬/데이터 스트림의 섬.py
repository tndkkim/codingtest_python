import sys
import re

input = sys.stdin.readline

num = int(input())


for i in range(num):
    T = list(map(int, input().split()))
    T.pop(0)
    n = len(T)
    count = 0
    for start in range(1, n-1):
        for end in range(start, n-1):
            sub = T[start:end+1]
            left = T[start-1]
            right = T[end+1]
            if all(x > left for x in sub) and all(x > right for x in sub):
                count += 1
    print(i+1, count)
                
        
    