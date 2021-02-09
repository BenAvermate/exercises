import math

def is_prime(n):
    if n == 0 or n == 1:
        return False
    x = math.floor(math.sqrt(n))
    for i in range(2,x+1):
        if (n % i) == 0:
            return False
    return True
    #return n>1 zou beter zijn