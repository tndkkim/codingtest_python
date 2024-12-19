N = int(input())
for _ in range(N):
   total = sum(ord(c)-64 for c in input() if c.isalpha())
   print("PERFECT LIFE" if total == 100 else total)