import re
with open("output.txt","w") as out:
    with open("input.txt") as inp:
        for line in inp:
            line = re.sub(r'\$HEX\((\d+)\)',lambda repl: "0x" + hex(int(repl.group(1))).upper()[2:],line)
            out.write(line)