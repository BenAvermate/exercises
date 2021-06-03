import textwrap
with open("input.txt") as lees:
    with open("output.txt","w") as schrijf:
        print(i for i in range(100))
        print("\n".join(textwrap.wrap(lees.readline(),40)),file=schrijf)