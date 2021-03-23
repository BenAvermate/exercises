import sys
import re

for file in sys.argv[1:]:
    with open(file,'r')as reading:
        inhoud = reading.read()
    inhoud = re.sub('#.*$','',inhoud, flags=re.MULTILINE)
    
    with open(file, 'w') as edit:
        edit.write(inhoud)