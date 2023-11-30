function solution(n, m) {
    var answer = [];
    //유클리드 호제법 함수
    function god(a, b){
        while(b!=0){
            let temp = b;
            b = a%b;
            a = temp;
        }
        return a;
    }
    //최대 공약수
    let c = god(n,m);
    //최소 공배수
    let d = (n*m)/c;
    
    answer.push(c, d);
    return answer;
}

//유클리드 호제법 함수
//god 함수: 유클리드 호제법을 사용하여 두 수의 최대 공약수를 계산하는 함수입니다. 
//두 수 a와 b의 최대 공약수는 a를 b로 나눈 나머지와 b의 최대 공약수와 동일합니다. 
//이를 반복하여 나머지가 0이 될 때까지 계산합니다.