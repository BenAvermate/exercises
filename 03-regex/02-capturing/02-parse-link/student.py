import re
def parse_link(string):
    match = re.fullmatch(r'<a href="(.*)">(.*)</a>',string)
    if match:
        url, text = match.groups()
        return (text, url)
    else :
        return None