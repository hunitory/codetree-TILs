const fs = require("fs");

let [a, b] = fs.readFileSync(0).toString().trim().split(" ").map(Number);

if (a >= 90) {
    if (b >= 95) {
        console.log(100000)
    } else if (b >= 90) {
        console.log(50000)
    } else {
        console.log(0)
    }
} else {
    console.log(0)
}