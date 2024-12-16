n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

picture_count = 0
max_size = 0

def DFS(graph, start_node): #--> 그림의 크기 반환환
    need_visit = [start_node]  #앞으로 방문해야하는 위치 저장용 스택  
    size = 0 #현재 탐색 중인 그림의 크기 저장용
    
    while need_visit: #모든 곳을 방문할 때까지 반복
        node = need_visit.pop() #스택의 가장 위에 값 꺼내기
        x, y = node
        
        if graph[x][y] == 1: #색칠된 부분인 경우
            graph[x][y] = 0 #방문한 곳으로 처리
            size += 1 #그림의 크기 + 1      
            
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx = x + dx #다음에 이동할 죄표 계산
                ny = y + dy     
                
                if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]): #다음에 이동할 죄표가 범위 내인지 확인인
                    if graph[nx][ny] == 1: #다음 좌표가 색칠된 부분인 경우
                        need_visit.append((nx,ny)) #스택에 
    
    return size


for i in range(n): #도화지의 모든 위치에서
    for j in range(m):
        if graph[i][j] == 1: #색칠된 부분이 있으면
            picture_count += 1 #그림 개수 증가
            max_size = max(max_size, DFS(graph, (i,j))) #dfs로 현재 그림 크기 구하기 -> 최대 크기 갱신

print(picture_count)
print(max_size)