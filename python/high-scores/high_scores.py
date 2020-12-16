def latest(scores):
    if scores==[]:
        raise Exception("Function cannot be called with an empty array")
    return scores[-1]


def personal_best(scores):
    if scores==[]:
        raise Exception("Function cannot be called with an empty array")
    largest = 0
    for i in range(1, len(scores) + 1):
        j = i - 1
        if scores[j] > largest:
            largest = scores[j]
    return largest


def personal_top_three(scores):
    if scores==[]:
        raise Exception("Function cannot be called with an empty array")
    for i in range(1, len(scores)):
        key = scores[i]
        j = i - 1
        while j >= 0 and key > scores[j]:
            scores[j + 1] = scores[j]
            j -= 1
        scores[j + 1] = key
    return scores[:3]
