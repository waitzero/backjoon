def solution(my_string):
    answer = ''
    a = list(my_string)
    m='aeiou'
    for i in my_string:
        if i not in m:
                answer += i
                
    return answer


#     문제 설명
# 영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다. 문자열 my_string이 매개변수로 주어질 때 모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.