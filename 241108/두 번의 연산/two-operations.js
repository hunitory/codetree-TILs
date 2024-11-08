const fs = require("fs");

let a = fs.readFileSync(0).toString().trim()

a = Number(a);

if ( a % 2 === 1) {
    a += 3;
}

if ( a % 3 === 0) {
    a /= 3;
}

console.log(a);