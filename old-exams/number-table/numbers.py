with open("output.txt","w") as out:
    for i in range(10001):
        binairy = bin(i)
        hexadecimal = hex(i)
        n = str(i).rjust(10)
        nb = str(binairy).rjust(20)
        nh = str(hexadecimal).rjust(10)
        print(f'{n}{nb}{nh}',file=out)