import re
from datetime import datetime
with open("output.txt","w") as output:
    with open("input.txt") as dates:
        for date in dates:
            correct=True
            try:
                datetime.strptime(date.strip(), "%d-%m-%Y")
            except ValueError:
                correct= False
            if correct:
                output.write(date)