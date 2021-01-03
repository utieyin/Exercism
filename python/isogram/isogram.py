def is_isogram(string):
    string = string.lower()
    for i in string:
        if string.count(i)>1 and (i not in [" ", "-"]):
            return False
    return True