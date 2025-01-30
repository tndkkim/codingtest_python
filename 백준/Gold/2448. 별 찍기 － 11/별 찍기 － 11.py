n=int(input())
g=[[' ']*2*n for _ in range(n)]
def s(x,y,n):
   if n==3:
       g[x][y]='*'
       g[x+1][y-1]=g[x+1][y+1]='*'
       for i in range(-2,3):g[x+2][y+i]='*'
       return
   m=n//2
   s(x,y,m)
   s(x+m,y-m,m)
   s(x+m,y+m,m)
s(0,n-1,n)
for i in g:print(''.join(i))