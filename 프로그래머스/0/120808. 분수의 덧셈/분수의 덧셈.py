import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    
    numer3 = (numer1 * denom2) + (numer2 * denom1)
    denom3 = denom1 * denom2
    
    gcd = math.gcd(numer3, denom3)
    
    answer = [numer3//gcd, denom3//gcd]
    return answer