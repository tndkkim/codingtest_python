import sys
input = sys.stdin.readline
N = int(input())

def round2(number):
    if number >= 0:
        return int(number + 0.5)
    else:
        return int(number - 0.5)

if N == 0:
    print(0)
else:
    nums = [int(input()) for _ in range(N)]
    nums.sort()
    
    delete = round2(N * 0.15)

    if delete >= N/2:
        print(round2(sum(nums)/N))
    else:
        nums = nums[delete:N-delete]
        print(round2(sum(nums)/len(nums)))