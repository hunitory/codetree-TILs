const fs = require("fs");

let n = Number(fs.readFileSync(0).toString().trim())

let check_num = 0;

for (let i = 1; i <= parseInt(n / 2); i++) {
    if (n % i === 0) {
        check_num += i
    }
}

if (check_num === n) {
    console.log("P")
} else {
    console.log("N")
}