with open("output.txt","w") as out:
    with open("input.txt") as names:
        for name in names:
            fname, lname = name.lower().strip().split(" ",1)
            lname="".join(lname.split())
            out.write(f'{fname}.{lname}@student.ucll.be\n')