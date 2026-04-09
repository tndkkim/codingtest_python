import sys
input = sys.stdin.readline

MOD = 1_000_000_007

def mat_mul(A, B):
    return [
        [(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD,
         (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD],
        [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD,
         (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD],
    ]

def mat_pow(M, n):
    result = [[1,0],[0,1]]
    while n:
        if n % 2 == 1:
            result = mat_mul(result, M)
        M = mat_mul(M, M)
        n //= 2
    return result

n = int(input())

if n == 1:
    print(1)
else:
    M = [[1,1],[1,0]]
    result = mat_pow(M, n)
    print(result[0][1])