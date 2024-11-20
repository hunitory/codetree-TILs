const fs = require("fs");

let n = Number(fs.readFileSync(0).toString().trim());

let ccnt = 0, bcnt = 0, tcnt = 0;

for (let i = 1; i <= n; i ++) {
    if (i % 12 === 0) {
        tcnt++
    } else if (i % 3 === 0) {
        bcnt++
    } else if (i % 2 === 0) {
        ccnt++
    }
}
console.log(`${ccnt} ${bcnt} ${tcnt}`)