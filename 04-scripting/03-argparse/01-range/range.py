import argparse

parser = argparse.ArgumentParser(prog='range')

parser.add_argument('start',type=int, help='Starting value')
parser.add_argument('end',type=int,help='Ending value (inclusive by default)')
parser.add_argument('-x','--exclusive',action='store_true', help='Ending value is exclusive')
parser.add_argument('--step',type=int, default=1,help='Step size (default=1)')

args = parser.parse_args()

#print(args)

i = args.start
if args.exclusive:
    while i < args.end:
        print(i)
        i += args.step
else:
    while i<= args.end:
        print(i)
        i += args.step