N = int(input())

if N == 1:
    print(1)
else:
    room = 1
    ans = 1
    
    while True:
        room += 6 * ans
        if N <= room:
            print(ans + 1)
            break
        ans += 1