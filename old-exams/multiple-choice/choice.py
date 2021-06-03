import csv
with open("solutions.csv") as solutions:
    solutions= tuple(solutions.read().strip().split(','))
    with open("output.txt","w") as out:
        with open("answers.csv") as answersFile:
            answersAll = csv.reader(answersFile)
            for student in answersAll:
                score=0
                student,answers= student[0],student[1:]
                for q in range(len(solutions)):
                    if answers[q]==solutions[q]:
                        score+=1
                print(student + " " + str(score),file=out)
            print(solutions)