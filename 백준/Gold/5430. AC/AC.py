from collections import deque

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    arr = input()[1:-1]
    dq = deque(map(int, arr.split(',')) if arr else [])
    rev = False
    err = False
    
    for cmd in p:
        if cmd == 'R':
            rev = not rev
        else:
            if not dq:
                err = True
                break
            dq.popleft() if not rev else dq.pop()
            
    if err:
        print('error')
    else:
        if rev:
            dq.reverse()
        print('[' + ','.join(map(str, dq)) + ']')