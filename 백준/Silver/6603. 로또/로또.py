import sys
input = sys.stdin.readline

while True:

    nums = list(map(int, input().split()))
    k =  nums.pop(0)

    if k == 0:
        break

    else:
        stack = []

        def DFS(start):
            if len(stack) == 6:
                print(*stack)
            for i in range(start, k):
                stack.append(nums[i])

                DFS(i+1)
                stack.pop()

        DFS(0)
        print()
