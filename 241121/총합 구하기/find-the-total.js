const fs = require("fs");
let [a, b] = fs.readFileSync(0).toString().trim().split(" ").map(Number);

let ans = 0;

for (a; a <= b; a++) {
    if (a % 6 === 0 && a % 8 != 0) {
        ans += a
    }
}

console.log(ans);