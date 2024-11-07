const fs = require("fs");

let call = fs.readFileSync(0).toString().trim();

call = Number(call);

if (call === 1) {
    console.log("John");
} else if (call === 2) {
    console.log("Tom");
} else if (call === 3) {
    console.log("Paul")
} else {
    console.log("Vacancy")
}