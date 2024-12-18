n = int(input())
cnt = 0
output = 666

while True:
    if '666' in str(output):
        cnt += 1
    if cnt == n:
        break
    output += 1

print(output)