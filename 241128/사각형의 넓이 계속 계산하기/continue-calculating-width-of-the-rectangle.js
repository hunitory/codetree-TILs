const fs = require("fs");

let input = fs.readFileSync(0).toString().trim().split("\n")

for (let index = 0; index < input.length ; index++ ) {
    let [a, b, c] = input[index].split(" ")
    console.log( Number(a) * Number(b));
    if (c === 'C') {
        break;
    }
}