const fs = require("fs");

input = fs.readFileSync(0).toString();

input = Number(input);


let ft = 30.48;

console.log((ft * input).toFixed(1) )