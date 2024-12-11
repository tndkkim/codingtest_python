import sys
from bisect import bisect_left
input = sys.stdin.readline

M, N = map(int, input().split()) #조카의 수 M,  과자의 수 N
lenN = list(map(int, input().split()))

lenN.sort() #457 549 743 802

left = 1
right = max(lenN)

def binary_search(M, left, right):
    if left>right:
        return right
    
    mid = (left + right) // 2
    cnt = 0
    
    for i in lenN:
        cnt += i // mid
        
    if cnt == M:
        return binary_search(M, mid + 1, right)
    elif cnt > M:
        return binary_search(M, mid + 1, right)
    else: #cnt < M
        return binary_search(M, left, mid - 1)
    
output = binary_search(M, left, right)
print(output)