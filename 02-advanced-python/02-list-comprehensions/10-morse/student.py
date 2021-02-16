def to_morse(string):
    return "   ".join([" ".join([code[char] for char in word]) for word in string.upper().split(" ")])
def from_morse(string):
    return " ".join( ["".join([ reverse_code[char] for char in word.split(" ")]) for word in string.split("   ")])


code = {
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",
}
reverse_code = dict( (y,x) for x,y in code.items())