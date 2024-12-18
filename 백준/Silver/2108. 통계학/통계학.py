from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

print(round(sum(nums)/N))

nums.sort()
print(nums[N//2])

cnt = Counter(nums)
max_cnt = max(cnt.values())
list = []
for i in sorted(cnt):
    if cnt[i] == max_cnt:
        list.append(i)
print(list[1] if len(list) > 1 else list[0])

print(nums[-1] - nums[0])
