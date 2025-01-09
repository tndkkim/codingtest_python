n = int(input())
count = 0
for _ in range(n):
    days = int(input().split('-')[1])
    if days <= 90:
        count += 1
print(count)