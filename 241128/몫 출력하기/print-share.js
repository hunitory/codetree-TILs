// 변수 선언 및 입력
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");

let index = 0;
let cnt = 0;

// 언제 끝날지 모르므로
// 계속 반복합니다.
while (true) {
    // 입력을 받습니다.
    let n = Number(input[index]);
    index++;
    
    // n이 홀수라면 아무 작업도 하지 않고, n이 짝수라면 n/2를 출력하는 작업을 3번 한 뒤 종료합니다.
    let result = n;
    if (n % 2 === 0) {
        result = parseInt(n / 2);
        cnt++;
    }
    else {
        continue;
    }
    console.log(result);
    if (cnt >= 3) {
        break;
    }
}