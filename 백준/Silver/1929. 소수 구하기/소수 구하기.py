M, N = map(int, input().split())

# 초기화: N+1 크기의 리스트를 True로 채움
is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False

# 에라토스테네스의 체 적용
i = 2
while i * i <= N:
    if is_prime[i]:
        # i의 배수들을 모두 False로 변경
        for j in range(i * i, N + 1, i):
            is_prime[j] = False
    i += 1

# M부터 N까지의 소수 출력
for i in range(M, N + 1):
    if is_prime[i]:
        print(i)