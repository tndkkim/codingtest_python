import sys
from collections import defaultdict
from math import comb
from bisect import bisect_left

input = sys.stdin.readline

M, N = map(int, input().split())
pattern_count = defaultdict(int)

for _ in range(M):
    planets = list(map(int, input().split()))
    tmp = sorted(list(set(planets)))
    pattern = [bisect_left(tmp, x) for x in planets]
    pattern_count[tuple(pattern)] += 1

result = sum(comb(count, 2) for count in pattern_count.values())
print(result)