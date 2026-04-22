import sys
import re

input = sys.stdin.readline

num = int(input())


for i in range(num):
    T = list(map(int, input().split()))
    T.pop(0)
    stack = [0]
    count = 0
    for t in T:
        if t > stack[-1]:
            stack.append(t)
            count += 1
        elif t == stack[-1]:
            continue
        else:
            while stack[-1] > t:
                stack.pop()
            if stack[-1] < t:
                stack.append(t)
                count += 1
    print(i+1, count)