import re


def count_words(sentence):
    sentence_list = [
        x.lower().strip("''!!&@$%^&") for x in re.split("[_, .\t\n:]", sentence) if x
    ]
    result = {}
    for x in sentence_list:
        result[x] = sentence_list.count(x)
    return result