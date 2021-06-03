import csv

result ={}
with open('exam-schedule.csv') as examschedule:
    data=csv.DictReader(examschedule)

    for line in data:
        lokaal = line["Lokaal"].strip()
        datum = line["Datum"].strip()
        dagdeel = line["Dagdeel"].strip()

        tabel = result.setdefault(lokaal,{})
        key= (datum,dagdeel)
        #0 is default value ipv None
        tabel[key]= tabel.get(key,0)+1

lokalen = sorted(result.keys())

with open("output.txt","w") as output:
    for lokaal in lokalen:
        output.write(f'{lokaal} {max(result[lokaal].values())}\n')