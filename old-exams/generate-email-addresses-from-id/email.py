with open("output.txt","w") as out:
    with open("input.txt") as ids:
        for id in ids:
            id = id.lower().strip()
            if id[0]== "u":
                out.write(f'{id}@ucll.be\n')
            else:
                out.write(f'{id}@student.ucll.be\n')