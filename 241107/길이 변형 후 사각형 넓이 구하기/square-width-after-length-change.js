const fs = require("fs");

let [a, b] = fs.readFileSync(0).toString().trim().split(' ').map(Number);

a += 8;
b *= 3;

console.log(a);
console.log(b);
console.log(a * b);