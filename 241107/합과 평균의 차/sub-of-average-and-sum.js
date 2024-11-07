const fs = require("fs")

let [a, b, c] = fs.readFileSync(0).toString().trim().split(" ").map(Number);

let sum = a + b + c;
let avg = (a + b + c) / 3

console.log(sum);
console.log(avg);
console.log(sum - avg)