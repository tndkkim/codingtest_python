n = int(input())
max_dp = [0] * 3
min_dp = [0] * 3

for i in range(n):
   a, b, c = map(int, input().split())
   
   temp_max = max_dp[:]
   temp_min = min_dp[:]
   
   max_dp[0] = max(temp_max[0], temp_max[1]) + a
   max_dp[1] = max(temp_max[0], temp_max[1], temp_max[2]) + b
   max_dp[2] = max(temp_max[1], temp_max[2]) + c
   
   min_dp[0] = min(temp_min[0], temp_min[1]) + a
   min_dp[1] = min(temp_min[0], temp_min[1], temp_min[2]) + b
   min_dp[2] = min(temp_min[1], temp_min[2]) + c

print(max(max_dp), min(min_dp))