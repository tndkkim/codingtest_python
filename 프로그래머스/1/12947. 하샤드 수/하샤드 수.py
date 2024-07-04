def solution(x):
    arr = list(map(int,str(x)))
    sum = 0
    for i in range(0, len(arr)):
        sum += arr[i]
    if (x % sum == 0): 
        return True
    else: 
        return False

        