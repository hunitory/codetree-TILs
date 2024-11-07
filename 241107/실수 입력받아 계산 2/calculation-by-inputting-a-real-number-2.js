const fs = require("fs");

let a = fs.readFileSync(0).toString();

a = Number(a);

console.log((a + 1.5).toFixed(2));