def solution(num_list):
    answer = num_list[0]
    a = len(num_list)
    for i in range(1, a):
        if a>=10:
            answer += num_list[i]
        else:
            answer *= num_list[i]
        
    return answer

#     문제 설명
# 정수가 담긴 리스트 num_list가 주어질 때,
#  리스트의 길이가 11 이상이면 리스트에 있는 모든 원소의 합을 10 이하이면 모든 원소의 곱을 return하도록 solution 함수를 완성해주세요.

