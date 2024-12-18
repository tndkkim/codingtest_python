M, N = map(int, input().split())

for num in range(M, N+1):
    if num < 2:
        continue
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
        if i * i > num:
            break

    if is_prime:
        print(num)