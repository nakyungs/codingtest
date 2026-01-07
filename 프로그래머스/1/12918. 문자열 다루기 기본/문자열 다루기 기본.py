def solution(s):
    answer = False
    if ((len(s) == 4) or (len(s) == 6)) and (s.isnumeric() == True):
        answer = True
    return answer