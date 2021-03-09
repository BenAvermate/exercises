import re

def thrice_repeated(string):
    return re.fullmatch(r'(.+)\1{2}',string)
    #return re.fullmatch(r'(.+)\1\1', string)