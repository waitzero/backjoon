def solution(numbers, n):
    answer = 0
    for i in range(len(numbers)):
        if answer<=n:
            answer += numbers[i]
    return answer

#     문제 설명
# 정수 배열 numbers와 정수 n이 매개변수로 주어집니다. numbers의 원소를 앞에서부터 하나씩 더하다가 그 합이 n보다 커지는 순간 이때까지 더했던 원소들의 합을 return 하는 solution 함수를 작성해 주세요.?