const fs = require("fs");

let [b, a] = fs.readFileSync(0).toString().trim().split(" ").map(Number);

while (a <= b) {
    if (b % 2 == 0) {
        process.stdout.write(`${b} `)
    }
    b--
}