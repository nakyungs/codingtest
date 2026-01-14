from collections import Counter
def solution(participant, completion):
    pset = Counter(participant)
    cset = Counter(completion)
    answer = pset - cset
    print(answer.keys())
    return list(answer.keys())[0]