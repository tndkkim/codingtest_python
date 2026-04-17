import sys
import re

input = sys.stdin.readline

n = int(input())
participants = []

for _ in range(n):
    line = input().strip().rstrip(',').lstrip('[').rstrip(']')
    name = re.search(r'"name":"(\w+)"', line).group(1)
    score = int(re.search(r'"score":(\d+)', line).group(1))
    hidden = int(re.search(r'"isHidden":(\d)', line).group(1))
    participants.append((name, score, hidden))

sorted_all = sorted(participants, key=lambda x: -x[1])

rank_map = {}
rank = 1
for i, (name, score, hidden) in enumerate(sorted_all):
    if i > 0 and score < sorted_all[i-1][1]:
        rank = i + 1
    rank_map[name] = rank

public = [(name, score) for name, score, hidden in participants if hidden == 0]

public.sort(key=lambda x: (rank_map[x[0]], x[0]))

for name, score in public:
    print(rank_map[name], name, score)