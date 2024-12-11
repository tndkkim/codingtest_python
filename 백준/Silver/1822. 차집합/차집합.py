import sys
input = sys.stdin.readline

lenA, lenB = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

onlyA = A - B
onlyA = sorted(onlyA)

print(len(onlyA))
if onlyA:
    print(*onlyA)
