s = input()
i = 0
result = ''
vowels = 'aeiou'

while i < len(s):
    result += s[i]
    if s[i] in vowels and i + 2 < len(s):
        if s[i+1] == 'p' and s[i+2] == s[i]:
            i += 2
    i += 1

print(result)