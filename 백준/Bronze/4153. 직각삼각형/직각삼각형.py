import sys
input = sys.stdin.readline

while True:
    nums = sorted(list(map(int, input().split())))
    if sum(nums) == 0:
        break
    print("right" if nums[2]**2 == nums[0]**2 + nums[1]**2 else "wrong")