import sys
x = list(sys.stdin.readline())
stack = [] #괄호 저장용
tmp = 1 #현재 계산 중인 값
answer = 0 #최종 점수
pre=''#직전 괄호 (i-1)
for i in x:
    if i == '(':
        stack.append(i)
        tmp *= 2
    elif i == '[':
        stack.append(i)
        tmp *= 3
    elif i == ')':
        if not stack or stack[-1] == '[': #스택이 비어있거나 마지막 괄호가 [면
            answer = 0 #올바르지 못함
            break
        elif pre == '(':
            answer += tmp
        stack.pop() #스택에서 마지막괄호 제거
        tmp //= 2 #tmp 초기화
    elif i == ']':
        if not stack or stack[-1] == '(':
            answer = 0
            break
        elif pre == '[':
            answer += tmp
        stack.pop()
        tmp //= 3
    pre = i
print(0 if stack else answer)
        
            