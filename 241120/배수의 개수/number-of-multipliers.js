const fs = require("fs");

let inputs = fs.readFileSync(0).toString().trim().split("\n").map(Number);

let ans3 = 0, ans5 = 0;

for (let i = 0; i <= 9; i++) {
    if (inputs[i] % 3 === 0) {
        ans3++
    } 
    if (inputs[i] % 5 === 0) {
        ans5++
    }
}
console.log(`${ans3} ${ans5}`)