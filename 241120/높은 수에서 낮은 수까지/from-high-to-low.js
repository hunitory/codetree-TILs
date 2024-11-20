const fs = require("fs");

let [a, b] = fs.readFileSync(0).toString().trim().split(" ").map(Number);

if (a >= b) {
    for (let i = 0; i <= a - b; i ++){
        process.stdout.write(`${a - i} `);
    }
} else {
    for (let i = 0; i <= b - a; i ++){
        process.stdout.write(`${b - i} `);
    }    
}