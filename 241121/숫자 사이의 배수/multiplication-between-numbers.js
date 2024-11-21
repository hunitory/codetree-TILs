const fs = require("fs");

let [a, b] = fs.readFileSync(0).toString().trim().split(" ").map(Number);


let ansSum = 0;
let cnt = 0;

for (a; a<= b; a++) {
    if ( a % 5 === 0 || a % 7 === 0) {
        ansSum += a
        cnt++
    }
}

console.log(`${ansSum} ${(ansSum / cnt).toFixed(1)}`)