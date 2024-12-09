N = int(input())
meeting = []
for _ in range(N):
    start, end = map(int, input().split())
    meeting.append((start, end))

meeting.sort(key=lambda x : (x[1], x[0]))

cnt = 0 #회의 개수
last = 0 #마지막 회의 끝 시간

for start, end in meeting:
    if start>=last:
        cnt += 1
        last = end
print(cnt)