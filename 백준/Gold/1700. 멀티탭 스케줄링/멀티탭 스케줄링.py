import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
names = list(map(int, input().strip().split()))

use = []
count = 0

#처음 N개 꽂기
for i in range(N):
    if names[i] not in use:
        use.append(names[i])

#N개를 제외한 나머지에서서
for i in range(N, K):
    # 이미 꽂혀있는 경우
    if names[i] in use:
        continue
    
    #빈 자리가 있는 경우
    if len(use) < N:
        use.append(names[i])
        continue

    #제거할 것 선택
    remove = use[0]
    
    #더이상 안쓰는 제품 찾기기
    for j in use:
        if j not in names[i:]:
            remove = j
            break
            
    #모두 나중에 사용되는 경우
    if remove in names[i:]:
        latest_idx = 0 #제일 나중에 사용되는는
        for j in use:
            next_idx = names[i:].index(j)
            if next_idx > latest_idx:
                latest_idx = next_idx
                remove = j
    
    #바꾸기
    use[use.index(remove)] = names[i]
    count += 1

print(count)