def solution(numbers):
    answer = 0
    j = max(numbers)
    k = numbers.index(j)
    numbers.pop(k)
    l= max(numbers)
    return j*l

#chat Gpt
def solution(numbers):
    max_value = max(numbers)
    numbers.remove(max_value)
    return max(numbers) * max_value



#문제 설명
#정수 배열 numbers가 매개변수로 주어집니다. 
#numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.