const fs = require("fs");

let n = Number(fs.readFileSync(0).toString().trim());

let cnt = 0;

while (n != 1) {
    if (n % 2 === 0) {
        n /= 2
    } else {
        n *= 3
        n++
    }
    cnt++
}

console.log(cnt);