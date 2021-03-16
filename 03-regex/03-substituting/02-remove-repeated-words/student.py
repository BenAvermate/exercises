import re
def remove_repeated_words(string):
    return re.sub(r'(\S+)(\s\1)+',r'\1',string)