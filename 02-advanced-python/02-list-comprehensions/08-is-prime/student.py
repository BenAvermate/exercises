def is_prime(n):
    return all(not n%m==0 for m in range(2,n)) and n>1