while True:
    line = input()
    stack = []
    
    if line == ".":
        break
    
    for i in line:
        if i == '[' or i == '(':
            stack.append(i)

        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break

    print('yes') if len(stack) == 0 else print('no')
    