import re
def hide_email_addresses(string):
    def replace(match):
        naam, at, com =match.groups()
        return "*"*(len(naam)+len(at)+len(com))
        #return "*"*len(match.group(0)) #geeft de hele string als group(0)
    return re.sub(r'(\S+)(@\S+)(\.\S+)',replace,string)