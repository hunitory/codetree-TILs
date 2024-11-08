const fs = require("fs");

let [a, b] = fs.readFileSync(0).toString().trim().split(" ").map(Number);

if (a < b) {
    console.log(1);
} else {
    console.log(0);
}

if (a == b) {
    console.log(1)
} else {
    console.log(0)
}