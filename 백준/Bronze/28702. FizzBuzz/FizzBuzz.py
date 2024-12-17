s1 = input()
s2 = input()
s3 = input()

if s1 not in ['Fizz', 'Buzz', 'FizzBuzz']:
    n = int(s1) + 3
elif s2 not in ['Fizz', 'Buzz', 'FizzBuzz']:
    n = int(s2) + 2
else:
    n = int(s3) + 1

if n%3==0 and n%5==0:
    print('FizzBuzz')
elif n%3==0:
    print('Fizz')
elif n%5==0:
    print('Buzz')
else:
    print(n)