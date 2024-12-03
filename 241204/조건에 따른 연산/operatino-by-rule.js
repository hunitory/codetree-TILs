const fs = require("fs");

let n = Number(fs.readFileSync(0).toString());

let cnt = 0;

while ( n < 1000) {
    if (n % 2 === 1) {
        n *= 3
        n++
    } else {
        n *= 2
        n += 2
    }
    cnt++
}

console.log(cnt - 1);