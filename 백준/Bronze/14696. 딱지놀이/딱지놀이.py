def count_shapes(arr):
    counts = [0] * 5
    for x in arr:
        counts[x] += 1
    return counts[4], counts[3], counts[2], counts[1]

n = int(input())
for _ in range(n):
    a = list(map(int, input().split()))[1:]
    b = list(map(int, input().split()))[1:]
    
    a_star, a_circle, a_square, a_triangle = count_shapes(a)
    b_star, b_circle, b_square, b_triangle = count_shapes(b)
    
    if a_star != b_star:
        print('A' if a_star > b_star else 'B')
    elif a_circle != b_circle:
        print('A' if a_circle > b_circle else 'B')
    elif a_square != b_square:
        print('A' if a_square > b_square else 'B')
    elif a_triangle != b_triangle:
        print('A' if a_triangle > b_triangle else 'B')
    else:
        print('D')