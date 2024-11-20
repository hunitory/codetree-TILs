const fs = require("fs")

let n = Number(fs.readFileSync(0).toString().trim())

let i = 1
while (i * 3 <= n) {
    process.stdout.write(`${i * 3} `)
    i++
}