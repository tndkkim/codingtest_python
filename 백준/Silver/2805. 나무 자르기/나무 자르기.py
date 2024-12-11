import sys
input = sys.stdin.readline

N, M = map(int, input().split()) #나무의 수 N,집으로 가져가려고 하는 나무의 길이 M
lenN = list(map(int, input().split()))

lenN.sort()

left = 0
right = max(lenN)

def total_tree(height):
    total = 0
    for i in lenN:
        if i>height:
            total += i - height
    return total

while left <= right:
    mid = (left + right) // 2
    tree_length = total_tree(mid)
    
    if tree_length >= M:
        output = mid
        left = mid + 1
    else:
        right = mid - 1
print(output)