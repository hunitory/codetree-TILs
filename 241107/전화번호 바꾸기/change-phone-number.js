const fs = require("fs");

let [f, s ,l] = fs.readFileSync(0).toString().trim().split('-');

console.log(`${f}-${l}-${s}`);