const fs = require("fs");

let [a, b] = fs.readFileSync(0).toString().trim().split(" ").map(Number);

for( b ; b >= a ; b-- ) {
    process.stdout.write(`${b} `)
}