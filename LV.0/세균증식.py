def solution(n, t):
    answer = n
    for i in range(1, t+1):
        answer += n
        n *= 2
    
    return answer



# 문제 설명
# 어떤 세균은 1시간에 두배만큼 증식한다고 합니다. 
# 처음 세균의 마리수 n과 경과한 시간 t가 매개변수로 주어질 때 t시간 후 세균의 수를 return하도록 solution 함수를 완성해주세요.

#배운점
#for문의 매개변수는 값을 더하면 초기화 하기떄문에 내부에서 대하는 로직을 만들어야함