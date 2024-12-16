import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

N = int(input())
A = list(map(int, input().strip().split()))
A.sort()
#print(A) #[-6, -5, -4, -4, 0, 1, 2, 2, 3, 7]
ans = 0

for i in range(N-2):
    start = i + 1
    end = N - 1
    
    while start < end:
        sum = A[i] + A[start] + A[end] #-4 1 3 = 0

        if sum == 0:
            if A[start] == A[end]: #start, end 인덱스가 같으면 
                ans += end - start #바로 빼서 몇 개 중복인지 개수 계산산
            else:
                cnt = end - bisect_left(A, A[end]) + 1 #start, end 인덱스가 다르면 end 인덱스가 몇 개 중복되는지 bisect로 계산
                ans += cnt
            start += 1  # start를 증가시켜줘야 함
        elif sum < 0:
            start += 1  # start를 증가시켜줘야 함
        else:
            end -= 1

print(ans)
