import sys
N = int(sys.stdin.readline())
vps = 0
for _ in range(N):
    x = list(sys.stdin.readline().strip())
    stack = []
    for i in x:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack:
                stack.append(i)
            elif stack[-1] == '(':
                stack.pop(-1)
    print('YES' if len(stack)==0 else 'NO')
     