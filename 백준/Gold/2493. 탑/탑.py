#탑의 수
N = int(input())
tower = list(map(int, input().split())) #타워 높이 리스트
stack = []
output = [0] * N

for i in range(N):
    while stack and tower[stack[-1]] <= tower[i]: #현재 탑 i 높이가 스택의 top보다 크다
        stack.pop()
    if stack:
        output[i] = stack[-1] + 1
        
    stack.append(i)
print(*output)