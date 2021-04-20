import argparse
import re
import sys

parser = argparse.ArgumentParser(prog='loc')
parser.add_argument('-e' '--count-empty-lines', help='Counts empty lines', dest='count_empty', action='store_true')
parser.add_argument('--comment',help='Comment identifier')
args=parser.parse_args()

skips = []

if not args.count_empty:
    skips.append(r'^\s*$')
if args.comment:
    skips.append(f'^\\s*{args.comment}')

count = 0
for line in sys.stdin:
    if not any(re.match(skip, line) for skip in skips):
        count+=1
print(count)