const fs = require("fs");

let n = Number(fs.readFileSync(0).toString().trim())

for ( n ; n >= 1 ; n-- ) {
    process.stdout.write(`${n} `)
}