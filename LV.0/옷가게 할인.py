def solution(price):
    answer = 0
    sale = 0
    if price >= 100000:
        sale = 5
    if price >= 300000:
        sale = 10
    if price >= 500000:
        sale = 20
    discount = price*sale/100
    answer = price - discount
    return int(answer)


# 문제 설명
# 머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
# 구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.