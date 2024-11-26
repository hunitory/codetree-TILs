const fs = require("fs");

let n = Number(fs.readFileSync(0).toString().trim());

let ans = 0;

for ( let i = 1; i <= n; i++ ) {
    ans += i
    if (ans >= n) {
        console.log(i);
        break;
    } 
}
