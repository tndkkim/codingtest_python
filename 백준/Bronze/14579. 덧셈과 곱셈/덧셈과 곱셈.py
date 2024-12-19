a,b=map(int,input().split())
r=1
for i in range(a,b+1):
    r=r*(i*(i+1)//2)%14579
print(r)