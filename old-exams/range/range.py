import time
with open("output.txt","w") as out:
    for i in range(100000):
        print(i+1,file=out)