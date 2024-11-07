const fs = require("fs");

let eyes = fs.readFileSync(0).toString().trim();

eyes = Number(eyes);

eyes >= 1.0 ? console.log('High') : eyes >= 0.5 ? console.log('Middle') : console.log('Low')