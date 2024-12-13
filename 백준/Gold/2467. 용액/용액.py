import sys
input = sys.stdin.readline

N = int(input())
value = list(map(int, input().split()))

left = 0
right = N-1
diff = abs(value[left]+ value[right])
ans = (value[left], value[right])

while left< right:
    sum = value[left] + value[right]

    if abs(sum) < diff:
        diff = abs(sum)
        ans = (value[left], value[right])
    if sum == 0:
        break
    elif sum < 0:
        left += 1
    else: 
        right -= 1
print(*ans)


