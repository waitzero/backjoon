def solution(s):
    answer = ''
    a = len(s)//2
    if len(s)% 2 == 1:
        answer = s[a]
    else:
        answer = s[a-1:a+1]
    return answer


#     가운데 글자 가져오기
# 문제 설명
# 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.