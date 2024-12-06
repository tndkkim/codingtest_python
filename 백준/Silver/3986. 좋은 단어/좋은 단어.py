import sys
N = int(sys.stdin.readline())
ans = 0
for _ in range(N):
    word = list(sys.stdin.readline().strip())
    stack = []
    
    for i in word:
        if not stack:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop(-1)
        else:
            stack.append(i)
            
    if len(stack) == 0:
        ans += 1
        
print(ans)
    