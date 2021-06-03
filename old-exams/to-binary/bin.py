with open("input.txt") as lees:
    with open("output.txt","w") as schrijf:
        for line in lees:
           print(bin(int(line))[2:],file=schrijf)