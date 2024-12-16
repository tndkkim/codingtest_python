import sys
input = sys.stdin.readline

T = input()

cnt = T.count('01')
cnt2 = T.count('10')
print(max(cnt, cnt2))