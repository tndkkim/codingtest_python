N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B_idx = [(b, i) for i, b in enumerate(B)]
B_idx.sort(reverse=True) # 내림차순 정렬
#print(B_idx) #[(8, 2), (7, 1), (3, 3), (2, 0), (1, 4)]
S = 0
for i in range(N):
    S+=A[i]*B_idx[i][0]
print(S)