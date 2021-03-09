import re

def starts_with_a(string):
    return re.search('^a',string)
    #return re.match('a',string)