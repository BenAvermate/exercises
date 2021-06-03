import re

def valid_time(h,m,s):
    return (int(h) in range(0,24)) and (int(m) in range(0,60)) and (int(s) in range(0,60))

with open('output.txt',"w") as output:
    with open("input.txt") as inp:
        i=0
        for line in inp:
            i+=1
            for match in [match for match in re.findall(r'(\d{1,2}):(\d{1,2}):(\d{1,2})', line)if not valid_time(*match)]:
                output.write(f'{i} {":".join(match)} \n')
