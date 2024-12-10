N = int(input())

pos = []
neg = []
one = []
zero = []

for i in range(N):
    value = int(input())
    if value > 1:
        pos.append(value)
    elif value == 0:
        zero.append(value)
    elif value == 1:
        one.append(value)
    else:
        neg.append(value)
        
pos.sort(reverse=True)
neg.sort()
sum = 0

if one:
    sum = len(one)

if pos:
    for i in range(0, len(pos)-1, 2):
        sum += pos[i]*pos[i+1]
    if len(pos) % 2 == 1:
        sum += pos[-1]
    
if neg:
    for i in range(0, len(neg)-1, 2):
        sum += neg[i]*neg[i+1]
    if len(neg) % 2 == 1:
        if not zero:
            sum += neg[-1]

print(sum)