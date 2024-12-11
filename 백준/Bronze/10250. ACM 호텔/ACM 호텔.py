T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())

    floor = N % H
    if floor == 0:
        floor = H

    room = (N - 1) // H + 1

    print(floor * 100 + room)