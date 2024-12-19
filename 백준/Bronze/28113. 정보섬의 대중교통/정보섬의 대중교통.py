import sys
input = sys.stdin.readline
N, A, B = map(int, input().strip().split())

if A < B:
    print('Bus')
elif A == B:
    print("Anything")
else:
    print("Subway")