const fs = require("fs");

input = fs.readFileSync(0).toString();

input = Number(input);

console.log((input * 2) + 3);