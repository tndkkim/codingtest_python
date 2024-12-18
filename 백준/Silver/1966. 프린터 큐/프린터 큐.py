test_cases = int(input())

for _ in range(test_cases):
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))
    
    documents = [(i, p) for i, p in enumerate(priorities)]
    count = 0
    
    while True:
        if documents[0][1] == max(doc[1] for doc in documents):
            count += 1
            if documents[0][0] == m:
                print(count)
                break
            documents.pop(0)
        else:
            documents.append(documents.pop(0))