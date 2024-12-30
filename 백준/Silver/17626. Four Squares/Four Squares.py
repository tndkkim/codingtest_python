n = int(input())

def is_square(n):
    return int(n ** 0.5) ** 2 == n

if is_square(n):
    print(1)
    exit()

for i in range(1, int(n ** 0.5) + 1):
    if is_square(n - i*i):
        print(2)
        exit()

for i in range(n):
    if i * i > n:
        break
    for j in range(i, n):
        if i*i + j*j > n:
            break
        if is_square(n - i*i - j*j):
            print(3)
            exit()

print(4)