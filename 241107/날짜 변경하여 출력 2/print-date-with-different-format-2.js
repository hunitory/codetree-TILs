const fs = require("fs")

let [a, b, c] = fs.readFileSync(0).toString().trim().split("-");

console.log(`${c}.${a}.${b}`)