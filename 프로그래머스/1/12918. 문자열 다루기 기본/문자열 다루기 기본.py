def solution(s):
    answer = False
    if (len(s) in [4, 6]) and (s.isnumeric() == True):
        answer = True
    return answer