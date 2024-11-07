const fs = require("fs");

let inputs = fs.readFileSync(0).toString().split("\n").map(Number);

inputs.forEach(input => {
    console.log(input.toFixed(3));
});