const fs = require("fs");

let inputs = fs.readFileSync(0).toString().trim().split("\n").map(Number);

let n = inputs[0];
let ans = 0;

for (let i = 1; i <= n; i++) {
    ans += inputs[i];
}

console.log(`${ans} ${(ans/n).toFixed(1)}`)