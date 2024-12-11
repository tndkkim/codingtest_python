import sys
import bisect
input = sys.stdin.readline

n = int(input())
lst1 = list(map(int,input().split()))
m = int(input())
lst2 = list(map(int,input().split()))
lst1.sort()

for i in lst2:
  if lst1[bisect.bisect(lst1,i)-1]==i : # 항목을 리스트에 넣을 때 넣어지는 자리에서 바로 왼쪽에 있는 것이 해당 숫자와 같은지 확인
    print(1) # 같으면 리스트 내에 해당 숫자가 있는 것이므로 1 반환
  else:
    print(0)