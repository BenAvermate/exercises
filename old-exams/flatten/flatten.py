with open("output.txt","w") as out:
    with open("input.txt") as nFlat:
        for line in nFlat:
            for number in line.strip().split(","):
                print(number, file=out)