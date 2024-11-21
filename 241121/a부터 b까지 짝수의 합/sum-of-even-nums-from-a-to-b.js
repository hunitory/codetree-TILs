const fs = require("fs");

let [a, b] = fs.readFileSync(0).toString().trim().split(" ").map(Number);

let ans = 0;

for (a; a <= b; a++) {
    if (a % 2 === 0) {
        ans += a;
    }
}

console.log(ans)