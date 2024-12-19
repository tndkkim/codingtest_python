N, M = map(int, input().split())
no_listen = set(input() for _ in range(N))
no_see = set(input() for _ in range(M))

no_listen_see = sorted(no_listen & no_see)
print(len(no_listen_see))
for name in no_listen_see:
   print(name)