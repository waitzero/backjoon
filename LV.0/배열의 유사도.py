def solution(s1, s2):
    a= -1
    answer=0
     
    ##재순이 풀이###
    if len(s1) < len(s2):
        for i in s1:
            if i in s2:
                answer += 1
    else:
        for i in s2:
            if i in s1:
                answer += 1
                
                
    
    #for e in range(len(s1)):
    #    a+=1
    #    for i in range(len(s2)):
    #        if (s1[a]==s2[i]):
    #            answer += 1
    # 2중 for문 시간복잡도 n*2떄문에 깔끔하지 몬함
        
    return answer



    #문제 설명
# 두 배열이 얼마나 유사한지 확인해보려고 합니다. 문자열 배열 s1과 s2가 주어질 때 같은 원소의 개수를 return하도록 solution 함수를 완성해주세요.
#in 은 배열에 중복값이 있는지 확인