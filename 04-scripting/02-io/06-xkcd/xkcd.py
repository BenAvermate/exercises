import sys
import urllib.request
import json
from PIL import Image

def get_data(n):
    if n :
        url= f'http://xkcd.com/{n}/info.0.json'
    else:
        url= 'http://xkcd.com/info.0.json'

    with urllib.request.urlopen(url) as site:
        info = site.read().decode('utf-8')
    
    return json.loads(info)


def get_image(url):
    with urllib.request.urlopen(url) as site:
        return Image.open(site)


data=get_data(None if len(sys.argv) ==1 else int(sys.argv[1]))

for key, value in data.items():
    print(f'{key}: {value}')

get_image(data['img']).show()