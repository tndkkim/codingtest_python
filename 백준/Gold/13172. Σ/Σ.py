def get_mod_inverse(a, m):
   def extended_gcd(a, b):
       if a == 0:
           return b, 0, 1
       gcd, x1, y1 = extended_gcd(b % a, a)
       x = y1 - (b // a) * x1
       y = x1
       return gcd, x, y

   _, x, _ = extended_gcd(a, m)
   return ((x % m) + m) % m

MOD = 1000000007
m = int(input())
result = 0

for _ in range(m):
   n, s = map(int, input().split())
   inv_n = get_mod_inverse(n, MOD)
   result = (result + (s * inv_n) % MOD) % MOD

print(result)