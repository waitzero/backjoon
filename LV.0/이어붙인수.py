def solution(num_list):
    answer = 0
    a =[]
    b =[]
    c = 0
    for i in range(len(num_list)):
        if num_list[i] % 2 == 1:
            a.append(num_list[i])
        else:
            b.append(num_list[i])
    c = ''.join(map(str, a))
    d = ''.join(map(str, b))
    answer = int(c)+int(d)
    
    return answer

# 문제 설명
# 정수가 담긴 리스트 num_list가 주어집니다.
#  num_list의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return하도록 solution 함수를 완성해주세요.

#배운점
#1-1 separator.join(iterable)
#   separator: 결합될 문자열 사이에 삽입할 구분 문자열입니다. 이것은 문자열을 결합할 때 각 문자열 사이에 삽입됩니다.
#   iterable: 결합할 문자열의 시퀀스(리스트, 튜플 등) 또는 반복 가능한 객체입니다.
#1-2 map(function, iterable)
#   function: 각 요소에 적용할 함수를 나타내는 함수 객체입니다.
#   iterable: 함수를 적용할 시퀀스 또는 반복 가능한 객체입니다