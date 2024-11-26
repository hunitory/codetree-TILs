const fs = require("fs");

let [a, b] = fs.readFileSync(0).toString().trim().split(" ").map(Number);

let ans = 1;

for (a; a <= b; a++) {
    ans *= a;
}

console.log(ans)