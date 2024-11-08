const fs = require("fs");

let a = Number(fs.readFileSync(0).toString().trim());

if (a % 2 === 0) {
    a /= 2
}

if ( a % 2 === 1) {
    a += 1
    a /= 2
}

console.log(a);