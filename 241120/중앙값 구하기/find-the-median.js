const fs = require("fs")

let numbers = fs.readFileSync(0).toString().trim().split(" ").map(Number)
numbers.sort((a, b) => a - b)

let [a, b, c] = [numbers[0], numbers[1], numbers[2]]

console.log(b)