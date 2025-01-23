while True:
    s = input()
    if s == '#':
        break
    print(sum(c.lower() in 'aeiou' for c in s))