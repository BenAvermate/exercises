def slug(string):
    strings = string.lower().split(" ")
    strings = strings[1:] + [strings[0]]
    return "-".join(strings)
    