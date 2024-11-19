const fs = require("fs");

let [a, b] = fs.readFileSync(0).toString().trim().split(" ").map(Number);

if (a >= 90) {
    if (b >= 95) {
        console.log(10)
    } else if (b >= 90) {
        console.log(5)
    } 
} else {
    console.log(0)
}