// 변수 선언 및 입력
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");

let cnt = 0;
for ( let index = 0 ;cnt < 3 ; index ++) {
    let n = Number(input[index]);

    if (n % 2 === 1) {
        continue
    } else {
        console.log(parseInt(n / 2));
        cnt++
    }
}