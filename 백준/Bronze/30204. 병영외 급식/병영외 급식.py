N, X = map(int, input().split())
p = list(map(int, input().split()))
s = sum(p)
print(1 if s % X == 0 else 0)