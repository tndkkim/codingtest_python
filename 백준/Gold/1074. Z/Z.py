N, r, c = map(int, input().split())
answer = 0

while N > 0:
    size = 2**(N-1)
    
    if r < size and c < size:
        pass
    elif r < size and c >= size:
        answer += size * size
        c -= size
    elif r >= size and c < size:
        answer += size * size * 2
        r -= size
    else:
        answer += size * size * 3
        r -= size
        c -= size
    N -= 1

print(answer)