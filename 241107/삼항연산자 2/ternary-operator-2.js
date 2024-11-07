const fs = require('fs');

let a = fs.readFileSync(0).toString().trim();

a = Number(a);

a === 1 ? console.log("t") : console.log("f")