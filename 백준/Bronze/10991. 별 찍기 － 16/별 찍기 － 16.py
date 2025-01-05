n = int(input())
for i in range(1, n+1):
    # 앞쪽 공백
    print(' ' * (n-i), end='')
    # 별과 공백 번갈아 출력
    for j in range(i):
        print('* ', end='')
    print()