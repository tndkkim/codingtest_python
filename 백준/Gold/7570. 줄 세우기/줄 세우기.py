import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().strip().split()))

max_len = 0
p = [0] * (1000001)  # 1e6+1

for num in nums:
    p[num] = p[num-1] + 1
    max_len = max(max_len, p[num])

print(N - max_len)