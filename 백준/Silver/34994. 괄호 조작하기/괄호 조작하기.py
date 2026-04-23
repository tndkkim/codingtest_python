import sys
input = sys.stdin.readline

def is_valid(S):
    stack = []
    pair = {')': '(', ']': '[', '}': '{'}
    for c in S:
        if c in '([{':
            stack.append(c)
        else:
            if not stack or stack[-1] != pair[c]:
                return False
            stack.pop()
    return len(stack) == 0

chars = '()[]{}'
N = int(input())
for _ in range(N):
    S = list(input().strip())
    n = len(S)
    
    if n % 2 == 1:
        print("NO")
        continue
    
    if is_valid(S):
        print("YES 0")
        continue
    
    found = False
    for i in range(n):
        for c in chars:
            if S[i] == c:
                continue
            orig = S[i]
            S[i] = c
            if is_valid(S):
                print("YES 1")
                print(i+1, c)
                found = True
                break
            S[i] = orig
        if found:
            break
    
    if not found:
        print("NO")