import sys
poly = sys.stdin.readline().strip().split('-')
edit_poly = []
idx = 0
for i in poly:
    if '+' in i:
        sum = 0
        nums = i.split('+')
        for j in nums:
            sum += int(j)
        edit_poly.append(sum)
    else:
        edit_poly.append(int(i))

output = edit_poly[0]
for i in range(1, len(edit_poly)):
    output -= edit_poly[i]
    
print(output)