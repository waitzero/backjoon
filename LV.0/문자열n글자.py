def solution(my_string, n):
    a = len(my_string)
    b = a-n
    c = my_string[b:a]
    return c

#     문제 설명
# 문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string의 뒤의 n글자로 이루어진 문자열을 return 하는 solution 함수를 작성해 주세요.

#배운점
#슬라이싱 =  문자열[시작 글자수: 끝 수]
#           문자열[::2] # 인덱스 0부터 끝까지, 2 스텝씩 건너뛰면서 자름 (HloWrd)
