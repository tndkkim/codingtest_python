import sys
input = sys.stdin.readline

N, C = map(int, input().split()) #마을 수, 트력 용량
M = int(input()) #박스 정보 개수

boxes = []
for _ in range(M):
    start, end, amount = map(int, input().split())
    boxes.append((start, end, amount))

boxes.sort(key=lambda x: (x[1], x[0]), reverse=True)
#print(boxes)

total = 0 #답
selected_box = []

for i in range(N, 0, -1):  # 가장 마지막 마을부터 반복
    capacity = C
    for start, end, amount in selected_box:
        if start < i and end > i:  # 현재 마을을 지나가는 박스
            capacity -= amount
    now_selected = []

    for start, end, amount in boxes:
        if end == i:  # 현재 도착지로 가는 박스만 선택
            possible = min(amount, capacity)
            if possible > 0:
                #print(f"{start}번 마을 -> {end}번 마을 ({possible}개)")
                now_selected.append((start, i, possible))
                capacity -= possible
                total += possible
            if capacity == 0:
                break

    selected_box.extend(now_selected)

print(total)