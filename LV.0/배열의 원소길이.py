def solution(strlist):
    mong=[]
    for i in strlist:
        mong.append(len(i))

    return mong


#     문제 설명
# 문자열 배열 strlist가 매개변수로 주어집니다. strlist 각 원소의 길이를 담은 배열을 retrun하도록 solution 함수를 완성해주세요.

#배운점
#1.배열.append(값) 배열 마지막에 값을 추가한다  ex) [0,1,2,3,{새로운값}] -리스트형태 
#1-1.배열.append([배열])을 사용하면 [0,1,2,3[값, 값]]이렇게 배열로 들어간다
#1-2.배열.extends([새로운 값])을 사용하면 [0,1,2,3,{새로운값}]으로 배열이 값으로 들어간다
#1-3.배열.insert(i,x)i 앞에 추가할 x를 삽입가능
