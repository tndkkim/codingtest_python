n, m = map(int, input().split())
passwords = {}

for _ in range(n):
    site, pwd = input().split()
    passwords[site] = pwd

for _ in range(m):
    site = input()
    print(passwords[site])