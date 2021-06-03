import re
with open("output.txt","w+") as output:
    with open("input.txt") as numbers:
        for number in numbers:
            if re.fullmatch(r'\+32-4[5-9]\d-\d{2}-\d{2}-\d{2}',number.strip()) or re.fullmatch(r'04[5-9]\d-\d{2}-\d{2}-\d{2}',number.strip()):
                output.write(number)
            