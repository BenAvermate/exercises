import argparse
import re
from PIL import Image
import os, sys
from pathlib import Path

def output_filename(pattern,input_file):
        path=Path(input_file)
        base = path.stem
        ext = path.suffix
        return pattern.replace('%b',base).replace('.%x',ext)
def size(s):
    match = re.fullmatch(r'(\d+)x(\d+)',s)
    if not match:
        print('Invalid size, pattern WxH')
    width, height =match.groups()
    return(int(width),int(height))

parser = argparse.ArgumentParser(prog='thumbnail')
parser.add_argument('files', help='Files',nargs='+')
parser.add_argument('--size', help='Size of thumbnail. (Default: 64x64)', default='64x64')
parser.add_argument('--pattern', help='Pattern for output files',default='%b-thumbnail.%x')
args = parser.parse_args()

size = size(args.size)
input_files = args.files
pattern = args.pattern

for input_file in input_files:
    output_file = output_filename(pattern,input_file)
    image = Image.open(input_file)
    image.thumbnail(size)
    image.save(output_file)