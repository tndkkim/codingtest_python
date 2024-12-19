import sys
input = sys.stdin.readline

M = int(input())
S = []
for _ in range(M):
    cmd = input().split()
    if len(cmd) == 2:
        cmd, x = cmd
        x = int(x)
    else:
        cmd = cmd[0]
        
    if cmd == 'add':
        if x not in S:
            S.append(x)
    elif cmd == 'remove':
        if x in S:
            S.remove(x)
    elif cmd == 'check':
        print(1 if x in S else 0)
    elif cmd == 'toggle':
        if x in S:
            S.remove(x)
        else:
            S.append(x)
    elif cmd == 'all':
        S = list(range(1, 21))
    elif cmd == 'empty':
        S = []