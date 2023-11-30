def solution(arr1, arr2):
    answer = 0
    a = 0
    b = 0
    if len(arr1) > len(arr2):
        return 1
    elif len(arr1) <len(arr2):
        return -1
    c = sum(arr1)
    d = sum(arr2)
    if c > d:
        return 1
    elif c<d:
        return -1
    else:
        return 0


#         문제 설명
# 이 문제에서 두 정수 배열의 대소관계를 다음과 같이 정의합니다.

# 두 배열의 길이가 다르다면, 배열의 길이가 긴 쪽이 더 큽니다.
# 배열의 길이가 같다면 각 배열에 있는 모든 원소의 합을 비교하여 다르다면 더 큰 쪽이 크고, 같다면 같습니다.
# 두 정수 배열 arr1과 arr2가 주어질 때, 위에서 정의한 배열의 대소관계에 대하여 arr2가 크다면 -1, arr1이 크다면 1, 두 배열이 같다면 0을 return 하는 solution 함수를 작성해 주세요.