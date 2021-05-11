import csv
import sys

def second(xs):
    return xs[1]

table = {}

with open("../title-episodes.tsv", encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter='\t',quoting=csv.QUOTE_NONE)
    for row in reader:
        id = row['parentTconst']
        if id not in table:
            table[id] = 0
        table[id] += 1

maxEP = max(table.values())
print(f'Max episodes count: {maxEP}')
series = { series_id for series_id, ep_count in table.items() if ep_count == maxEP}

with open("../title-basics.tsv", encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter='\t', quoting=csv.QUOTE_NONE)
    for row in reader:
        if row['tconst'] in series:
            print(row['primaryTitle'])