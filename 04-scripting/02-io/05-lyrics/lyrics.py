import sys
import re
import urllib.request
import json

title=re.sub('\s','%20',sys.argv[1])
artist=re.sub('\s','%20',sys.argv[2])

with urllib.request.urlopen(f'https://api.lyrics.ovh/v1/{artist}/{title}') as site:
    lyrics = json.loads(site.read())
    print(lyrics['lyrics'])