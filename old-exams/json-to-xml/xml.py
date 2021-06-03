import json

with open("input.json") as file:
    students = json.load(file)

with open("output.txt","w") as out:
    print("<students>",file=out)
    for student in students:
        id,grades= student["id"],student["grades"]
        string_grades="".join(f'<grade>{x}</grade>' for x in grades)
        print(f'<student id="{id}"><grades>{string_grades}</grades></student>',file=out)
    print("</students>",file=out)