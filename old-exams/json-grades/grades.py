import json
import math

with open("input.json") as jSon:
    data = json.load(jSon)

students = {}

for student in data:
    av = int(round(sum(student["grades"])/len(student["grades"])))
    students[student["id"]]=students.get(student["id"],0)+ av

students = sorted(students.items(), key= lambda item: item[0])

with open("output.txt","w")as out:
    for id, grade in students:
        out.write(f'{id} {grade}\n')