import re
with open("output.txt","w") as out:
    with open('input.txt') as commits:
        authors = {}
        for line in commits:
            if re.search('Author', line):
                parts = line.split()
                author = " ".join([part for part in parts[1:-1]])
                authors[author]= authors.get(author,0)+1
        for author in sorted(authors.items(), key=lambda item: item[1], reverse=True):
            print(author[0] +": " + str(author[1]), file=out)