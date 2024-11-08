const fs = require("fs");

let input = fs.readFileSync(0).toString().trim().split("\n").map(Number);

let left = input[0];

let right = input[1];

if (left >= 1.0 && right >= 1.0) {
    console.log("High");
} else if (left >= 0.5 && right >= 0.5) {
    console.log("Middle")
} else {
    console.log('Low')
}