import re

def is_valid_password(string):
    mandatory = [
        r'.{8,}',
        r'[0-9]',
        r'[a-z]',
        r'[A-Z]',
        r'[\+\-*/.@]',
    ]
    prohibited = [
        r'(.)\1{2}',
        r'(.)(.*\1){3}',
    ]
    return all(re.search(regex, string) for regex in mandatory) and not any(re.search(regex, string) for regex in prohibited)