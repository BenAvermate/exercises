import re

def is_valid_email_address(string):
    return re.fullmatch(r'[0-9a-z\.]+@(student\.)?ucll\.be',string)