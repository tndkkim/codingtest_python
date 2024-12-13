import sys
input = sys.stdin.readline

N = int(input())
numbers = [int(input()) for _ in range(N)]

numbers.sort()

possible = set()
for i in numbers:
    for j in numbers:
        possible.add(i+j)

answer = None
for i in range(N-1, -1, -1):
    found = False
    for j in range(i+1):
        if numbers[i] - numbers[j] in possible:
            answer = numbers[i]
            found = True
    if found: 
        break
print(answer)