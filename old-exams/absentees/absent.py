with open('./attending.txt') as attending:
    attenders = set( l.strip().lower() for l in attending)

with open('./all.txt') as all:
    with open('./absentees.txt','w') as absent:
            for student in all:
                student=student.strip().lower()
                if student not in attenders:
                    absent.write(f'{student}\n')