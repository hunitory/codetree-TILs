const fs = require("fs");

let n = fs.readFileSync(0).toString().trim()

n = Number(n)

for (let i = 1; i <= 5 ; i++) {
    process.stdout.write(`${n * i} `)
}