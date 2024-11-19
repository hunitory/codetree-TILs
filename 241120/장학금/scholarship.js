const fs = require("fs");

let [a, b] = fs.readFileSync(0).toString().trim().split(" ").map(Number);

if (a >= 90 && b >= 90) {
    console.log(b >= 95 ? 100000 : 50000);
} else {
    console.log(0);
}