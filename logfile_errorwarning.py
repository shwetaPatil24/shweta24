import re
path = r"C:\Users\Shilpa\Desktop\logfile.txt"
regex = 'WARNING'
 
parsedlist = []
with open(path, "r") as file:
    for line in file:
        print(line)
        for match in re.finditer(regex, line, re.S):
            match_text = match.group()
            parsedlist.append(match_text)
            print(parsedlist)
