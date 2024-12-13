N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

total_bundles = 0
for size in sizes:
    if size > 0:
        total_bundles += (size + T - 1) // T

pen_bundles = N // P
single_pens = N % P

print(total_bundles)
print(pen_bundles, single_pens)