def solution(my_string, is_suffix):
    answer = 0
    suffix=[]
    a = len(my_string)
    for i in range(len(my_string)):
        suffix.append(my_string[i: a])       
        if suffix[i] == is_suffix:
            return 1
    return 0

# 문제 설명
# 어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다. 예를 들어, "banana"의 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다.
# 문자열 my_string과 is_suffix가 주어질 때, is_suffix가 my_string의 접미사라면 1을, 아니면 0을 return 하는 solution 함수를 작성해 주세요.