def solution(s):
    words = s.split(" ")
    ans = []
    for word in words:
        new = ""
        for i in range(len(word)):
            if i % 2 == 0:
                new += word[i].upper()
            else:
                new += word[i].lower()
        ans.append(new)
    return " ".join(ans)