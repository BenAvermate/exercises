import argparse
import re
import os
from pathlib import Path

def min_size(size):
    def check(file):
        return os.path.getsize(file) >= size

parser = argparse.ArgumentParser(prog='find')
parser.add_argument('start', help='Directory from where to start searching', default='.')
parser.add_argument('--minimum-size', dest='min_size', type=int, help='Minimum file size to be listed', default=0)
parser.add_argument('--maximum-size', dest='max_size', type=int, help='Maximum file size to be listed', default=float('inf'))
parser.add_argument('--no-directories',dest='no_directories', action='store_true', default=False, help='Removes directories form list')
parser.add_argument('--no-files', dest='no_files', action='store_true', default=False, help='Removes files from list')
parser.add_argument('--extension', dest="ext", help='Extensions')
parser.add_argument('--contains', dest='contains', help='Contents must match')
args= parser.parse_args()

path=Path(args.start)
for entry in path.glob('**/*'):
    if not os.path.getsize(entry) >= args.min_size: continue
    if not os.path.getsize(entry) <= args.max_size: continue
    if args.no_directories and os.path.isdir(entry): continue
    if args.no_files and os.path.isfile(entry): continue
    if args.ext and not entry.suffix == args.ext: continue
    if args.contains:
        if not os.path.isfile(entry):
            continue
        with open(entry, 'r') as file:
            content = file.read()
            if not re.search(args.contains, content):
                continue
    print(entry)