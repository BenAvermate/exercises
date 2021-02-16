def format_grades(grades):
    grade = []
    for key in grades:
        grade.append(f'{key}: {round(sum(grades[key])/len(grades[key]))}')
    return "\n".join(grade)