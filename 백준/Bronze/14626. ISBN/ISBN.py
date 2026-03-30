import sys

isbn = list(input())
sum = 0
idx = 0
for i in range(len(isbn)-1):
    if isbn[i] != '*' and i%2 == 0:
        # print(isbn[i])
        sum += int(isbn[i])
    elif isbn[i] != '*' and i%2 == 1:
        sum += int(isbn[i])*3
    else:
        idx = i
        

# (* + sum) 이게 ~~~~0 135+~~    일련번호 3 -> x = 2
# 일련번호 isbn[-1]

ans = (10 - (sum + int(isbn[-1])) % 10) % 10
ans = ans if idx%2 ==0 else (ans * 7)%10
print(ans)