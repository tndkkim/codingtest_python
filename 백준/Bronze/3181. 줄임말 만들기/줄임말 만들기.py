ignore = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
words = input().split()
result = ''

for i, word in enumerate(words):
   if i == 0 or word not in ignore:
       result += word[0].upper()

print(result)