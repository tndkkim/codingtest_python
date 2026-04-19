def d(n):
    return n + sum(int(c) for c in str(n))

not_self = set()
for n in range(1, 10001):
    next_n = d(n)
    if next_n <= 10000:
        not_self.add(next_n)

for n in range(1, 10001):
    if n not in not_self:
        print(n)