const fs = require("fs");

let [a, b, c] = fs.readFileSync(0).toString().trim().split(" ").map(Number);

let ansA, ansB

if (a === Math.min(a,b,c)) {
    ansA = 1
} else {
    ansA = 0
}

if (a === b && a === c) {
    ansB = 1
} else {
    ansB = 0
}

console.log(`${ansA} ${ansB}`)