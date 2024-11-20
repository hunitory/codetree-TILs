const fs = require("fs")

let numbers = fs.readFileSync(0).toString().trim().split(" ").map(Number)
numbers.sort();
console.log(numbers[1]);