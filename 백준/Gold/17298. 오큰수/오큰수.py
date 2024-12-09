N=int(input())
num = list(map(int, input().split()))

stack = []
output = [-1] * N

for i in range(N):
    while stack and num[stack[-1]] < num[i]: #스택에 값이 있고 현재 수가 더 큼
        output[stack.pop()] = num[i]
    stack.append(i)
    
print(*output)