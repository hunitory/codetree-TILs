const fs = require("fs");

let inputs = fs.readFileSync(0).toString().split("\n").map(Number);

for (let i = 0; i < 3; i++) { 
    console.log(inputs[i].toFixed(3));
}