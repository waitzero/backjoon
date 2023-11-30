계속 파일 만들기 너무 귀찮아서 여기다 씀

def solution(rny_string):
    answer = ''
    
    return rny_string.replace('m', 'rn')

#     문제 설명
# 'm'과 "rn"이 모양이 비슷하게 생긴 점을 활용해 문자열에 장난을 하려고 합니다. 
# 문자열 rny_string이 주어질 때, rny_string의 모든 'm'을 "rn"으로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.


#배열원소 삭제하기
def solution(arr, delete_list):
    answer = []
    for i in range(len(arr)):
        if not arr[i] in delete_list:
            answer.append(arr[i])
    return answer


# 문제 설명
# 정수 배열 arr과 delete_list가 있습니다.
#arr의 원소 중 delete_list의 원소를 모두 삭제하고 남은 원소들은 기존의 arr에 있던 순서를 유지한 배열을 return 하는 solution 함수를 작성해 주세요.

# 조건에 맞게 수열 변환하기 3
# 문제 설명
# 정수 배열 arr와 자연수 k가 주어집니다.

# 만약 k가 홀수라면 arr의 모든 원소에 k를 곱하고, k가 짝수라면 arr의 모든 원소에 k를 더합니다.

# 이러한 변환을 마친 후의 arr를 return 하는 solution 함수를 완성해 주세요.
def solution(arr, k):
    answer = []
    if k%2 ==1:
        for i in range(len(arr)):
            answer.append(arr[i]*k)
    else:
        for i in range(len(arr)):
            answer.append(arr[i]+k)
    return answer






