import re
def scrape_email_addresses(string):
    return re.findall(r'\S+@\S+\.\S+',string)