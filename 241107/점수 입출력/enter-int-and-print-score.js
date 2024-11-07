const fs = require("fs");

num = fs.readFileSync(0).toString();

num = Number(num);

console.log(`Your score is ${num} point.`);