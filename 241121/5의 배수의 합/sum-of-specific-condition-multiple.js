const fs = require("fs");

let [a, b] = fs.readFileSync(0).toString().trim().split(" ").map(Number);

let minNum = Math.min(a, b);
let maxNum = Math.max(a, b);

let ans = 0;

for (minNum; minNum <= maxNum; minNum++) {
    if (minNum % 5 === 0) {
        ans += minNum;
    }
}

console.log(ans)