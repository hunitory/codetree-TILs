const fs = require("fs");

let [b, a] = fs.readFileSync(0).toString().trim().split(" ").map(Number);

for ( b ; b >= a ; b -= 2 ) {
    process.stdout.write(`${b} `)
}