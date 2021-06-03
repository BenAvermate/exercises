import csv

with open('output.txt',"w") as output:
    with open('exam-schedule.csv') as examschedule:
        results ={}
        exams = csv.DictReader(examschedule)

        for exam in exams:
            lectoren = exam["Lector"]
            soort = exam["Ex. Soortx"]
            lectoren = lectoren.split('/')
            if soort == "S":
                for lector in lectoren:
                    results[lector]=results.get(lector,0)+1
        #print(results)
        results=sorted(results.items())
        #print(results)

        output.write("\n".join(f'{lector} {n}' for lector,n in results))