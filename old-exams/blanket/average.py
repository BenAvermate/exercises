import json
from datetime import datetime
from statistics import mean

with open('input.txt') as file:
    data = [(datetime.strptime(date, '%d/%m/%Y'), temp) for date, temp in json.load(file).items()]

for _, temps in sorted(data, key=lambda p : p[0]):
    print(round(mean(temps)))