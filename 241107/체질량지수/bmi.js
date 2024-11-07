const fs = require("fs");

let [h, w] = fs.readFileSync(0).toString().trim().split(" ").map(Number);

const bmi = Math.floor((10000 * w) / (h * h))

if ( bmi >= 25 ) {
    console.log(bmi);
    console.log("Obesity");
} else {
    console.log(bmi);
}