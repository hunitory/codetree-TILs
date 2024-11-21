const fs = require("fs");

let n = Number(fs.readFileSync(0).toString().trim())

let ans = 0;

for (n; n <= 100; n++) {
    ans += n;
}

console.log(ans);