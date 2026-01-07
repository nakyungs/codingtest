def solution(t, p):
    answer = 0
    num = len(p)
    for i in range(len(t) - num + 1):
        if int(t[i:i + num]) <= int(p):
            answer += 1
    return answer