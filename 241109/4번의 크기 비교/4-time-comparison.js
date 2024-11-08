const fs = require("fs")

const input = fs.readFileSync(0).toString().trim().split("\n");

let a = input[0]

let [b, c, d, e] = input[1].split(" ").map(Number);

console.log(a > b ? 1 : 0);
console.log(a > c ? 1 : 0);
console.log(a > d ? 1 : 0);
console.log(a > e ? 1 : 0);