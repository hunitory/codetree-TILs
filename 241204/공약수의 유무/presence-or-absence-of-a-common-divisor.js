const fs = require("fs");

let [a, b] = fs.readFileSync(0).toString().trim().split(" ").map(Number);

let flag = false

for (let i = a; i <= b; i++) {
    if ( 1920 % i === 0 || 2880 % i === 0 ) {
        flag = true;
        break
    }
}

if (flag === false) {
    console.log(0)
} else {
    console.log(1)
}