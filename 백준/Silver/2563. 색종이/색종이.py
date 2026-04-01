num = int(input())
papers = []
for i in range(num):
    paper = list(map(int, input().split()))
    #print(paper)
    papers.append(paper)

grid = [[0] * 100 for _ in range(100)]

for i, j in papers:
    for k in range(10):
        for l in range(10):
            grid[i+k][j+l] = 1
total = 0          
for i in grid:
    total += sum(i)
    
print(total)