import re
import datetime

def datum(s):
    m=re.search(r'Date:\s+(.*)',s)
    date=m.group(1)
    return datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

with open('input.txt') as commits:
    input= commits.read()

commits=re.findall(r'commit.*?Closed \#\d+', input, re.DOTALL | re.MULTILINE)
commits.sort(key=datum , reverse=True)

with open("output.txt","w") as out:
    out.write("\n\n".join(commits))