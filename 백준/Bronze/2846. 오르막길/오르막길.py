n = int(input())
heights = list(map(int, input().split()))
max_climb = 0
current_start = heights[0]
for i in range(1, n):
   if heights[i] <= heights[i-1]:
       current_start = heights[i]
   else:
       max_climb = max(max_climb, heights[i] - current_start)
print(max_climb)