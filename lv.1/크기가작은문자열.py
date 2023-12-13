def solution(t, p):
    answer = 0
    number = []
    for i in range(len(t)-len(p)+1):
        a = t[i:i+len(p)]
        number.append(a)
        if number[i]<=p:
            answer+=1
    return answer