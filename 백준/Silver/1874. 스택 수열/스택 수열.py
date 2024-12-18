N = int(input())

nums = [int(input()) for _ in range(N)]
stack = []
count = 1
result = []

for i in range(N):
    while count <= nums[i]:
        stack.append(count)
        result.append('+')
        count += 1
    if stack[-1] == nums[i]:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit()

print('\n'.join(result))