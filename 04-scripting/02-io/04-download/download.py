import sys
import urllib.request

with urllib.request.urlopen(sys.argv[1]) as input:
    content =input.read()
    print(content)