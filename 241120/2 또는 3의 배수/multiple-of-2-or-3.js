const fs = require("fs");

let n = Number(fs.readFileSync(0).toString().trim());

for (let i = 1 ; i <= n; i++ ) {
    process.stdout.write(`${ i % 2 === 0 || i % 3 === 0 ? 1 : 0 } `)
}