import re

def twice_repeated(string):
    return re.fullmatch(r'(.)\1',string)
    #of return re.fullmatch('(.)\\1',string)