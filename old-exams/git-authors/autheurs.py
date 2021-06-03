import re
with open("output.txt","w") as out:
    with open('input.txt') as commits:
        authors = set()
        for line in commits:
            if re.search('Author', line):
                parts = line.split()
                author= " ".join([part for part in parts[1:-1]])
                authors.add(author)
        for author in sorted(authors):
            print(author, file=out)