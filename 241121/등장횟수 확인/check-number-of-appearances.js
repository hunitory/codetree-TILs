const fs = require("fs");

let inputs = fs.readFileSync(0).toString().trim().split("\n").map(Number);

let cnt = 0;

for (let i = 0; i < 5; i++ ) {
    if (inputs[i] % 2 === 0) {
        cnt++;
    }
}

console.log(cnt)