import sys
N = int(sys.stdin.readline())
#3월 1일부터 11월 30일, 최소 개수

def days(month, day): #총 며칠인지
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return sum(days[:month]) + day

flowers = [0] * N
for i in range(N):
    start_month, start_day, end_month, end_day = map(int, sys.stdin.readline().split())
    flowers[i] = (days(start_month, start_day), days(end_month, end_day) )
#4
# 1 1 5 31
# 1 1 6 30
# 5 15 8 31
# 6 10 12 10
#[(1, 151), (1, 181), (135, 243), (161, 344)]
    
# print(flowers)
flowers.sort(key=lambda x:(x[0], -x[1]))
must_start = days(3, 1) #60
must_end = days(11, 30) #334

# print(must_start)
# print(must_end)

cnt = 0 #꽃 개수
tmp = must_start
tmp_end = 0
i = 0
while tmp <= must_end:
    tmp_end = tmp
    while i<N and flowers[i][0] <= tmp:
        tmp_end = max(tmp_end, flowers[i][1])
        i += 1
    if tmp_end == tmp:  # 더 이상 진행할 수 없는 경우
        print(0)
        exit()
        
    cnt += 1
    tmp = tmp_end
    
    if tmp > must_end:
        break
            
print(cnt)