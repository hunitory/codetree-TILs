const fs = require("fs");

let input = fs.readFileSync(0).toString().trim().split('\n');

let a = input[0].split(" ").map(Number);
let b = input[1].split(" ").map(Number); 

if (a[0] > b[0] || (a[0] == b[0] && a[1] > b[1])) {
    console.log("A")
} else {
    console.log("B")
}