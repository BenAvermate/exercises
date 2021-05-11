import sys
from sys import argv
import csv

def create_reader(file):
    return csv.DictReader(file, delimiter='\t',quoting=csv.QUOTE_NONE)

s_name = argv[1]

with open("../title-basics.tsv",encoding='utf-8') as file:
    reader = create_reader(file)
    rows = [row for row in reader if row['originalTitle'] == s_name and row['titleType'] == 'tvSeries']

if len(rows) != 1:
    print(f'Found {len(rows)} matches')
    for match in rows:
        #print(match.keys())
        #print(match.values())
        print(match['originalTitle'], match['startYear'])
    sys.exit(-1)

row = rows[0]
s_id = row['tconst']

e_data = {}

with open('../title-episodes.tsv',encoding='utf-8') as file:
    reader = create_reader(file)
    for row in reader:
        if row['parentTconst'] == s_id:
            data = { 'season': int(row['seasonNumber']), 'episode number': int(row['episodeNumber'])}
            e_data[row['tconst']] = data

with open('../title-ratings.tsv',encoding='utf-8') as file:
    reader = create_reader(file)
    for row in reader:
        id = row['tconst']
        if id in e_data:
            e_data[id]['rating'] = float(row['averageRating'])

with open('../title-basics.tsv',encoding='utf-8') as file:
    reader = create_reader(file)
    for row in reader:
        id = row['tconst']
        if id in e_data:
            e_data[id]['title'] = row['originalTitle']

for data in sorted(e_data.values(), key=lambda data: data['rating'], reverse=True):
    title = data['title'].ljust(40, ' ')
    rating = data['rating']
    season = str(data['season']).rjust(2, '0')
    e_nr = str(data['episode number']).rjust(2, '0')
    print(f'S{season}E{e_nr} {title} {rating}')