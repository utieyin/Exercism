def score(word):
    scores={
        1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"], 
        2: ["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y" ],
        5: ["K"],
        8: ["J", "X"],
        10: ["Q", "Z"]
    }
    a=0
    if len(word)==0:
        return a
    else:
        word_list =[x.upper() for x in word]
        for i in scores:
            for g in word_list:
                if g in scores[i]:
                    a+=i

    return a

score("f")
