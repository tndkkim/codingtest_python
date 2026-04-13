ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
hundreds = ["", "onehundred", "twohundred", "threehundred", "fourhundred", "fivehundred",
            "sixhundred", "sevenhundred", "eighthundred", "ninehundred"]

def to_word(n):
    if n < 20:
        return ones[n]
    elif n < 100:
        return tens[n // 10] + ones[n % 10]
    else:
        return hundreds[n // 100] + to_word(n % 100)

N = int(input())
words = [input().strip() for _ in range(N)]

base = sum(len(w) for w in words if w != "$")

for n in range(1, 1000):
    word = to_word(n)
    if base + len(word) == n:
        print(" ".join(word if w == "$" else w for w in words))
        break