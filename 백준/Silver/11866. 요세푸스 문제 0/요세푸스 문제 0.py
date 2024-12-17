N, K = map(int, input().split())
people = list(range(1, N+1))
result = []
index = 0

while people:
   index = (index + K - 1) % len(people)
   result.append(str(people.pop(index)))

print('<' + ', '.join(result) + '>')