const fs = require("fs");

let [a, b] = fs.readFileSync(0).toString().trim().split(" ").map(Number);

let ansA, ansB;

if (a < b) {
    ansA = 1;
} else {
    ansA = 0;
}

if (a == b) {
    ansB = 1;
} else {
    ansB = 0;
}

console.log(ansA, ansB);