const fs = require("fs");

const inputs = fs.readFileSync(0).toString().trim().split("\n").map(Number);

let flag = true;

for ( const input of inputs ) {
    if (input === 1) {
        continue
    }

    if (input % 3 != 0) {
        flag = false;
        break
    }
}

if (flag) {
    console.log(1)
} else {
    console.log(0)
}