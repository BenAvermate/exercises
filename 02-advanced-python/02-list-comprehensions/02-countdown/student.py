def countdown(n):
    if (n==1):
        return '1'
    return f'{n}, ' + countdown(n-1)