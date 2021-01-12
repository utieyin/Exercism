import re
def abbreviate(words):
    words = [x for x in re.split("[-,_ \n]", words) if x]
    result=""
    for i in words:
        result=result+i[0].upper()
    return result