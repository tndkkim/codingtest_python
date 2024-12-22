import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_to_name = [''] * (N + 1)
name_to_num = {}

for i in range(1, N + 1):
   name = input().rstrip()
   num_to_name[i] = name
   name_to_num[name] = i

for _ in range(M):
   query = input().rstrip()
   if query.isdigit():
       print(num_to_name[int(query)])
   else:
       print(name_to_num[query])