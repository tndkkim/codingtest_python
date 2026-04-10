import sys
input = sys.stdin.readline

N, M = map(int, input().split())
true = list(map(int, input().split()))
true.pop(0)
true = set(true)

party = [[] for _ in range(M)]

for i in range(M):
    party[i] = list(map(int, input().split()))
    party[i].pop(0)

#print(*party)
while True:
    changed = False
    for i in range(M):
        if any(person in true for person in party[i]):
            before = len(true)
            true.update(party[i])
            if len(true) > before:
                changed = True
    if not changed:
        break

count = 0
for i in range(M):
    if not any(person in true for person in party[i]):
        count += 1

print(count)
        