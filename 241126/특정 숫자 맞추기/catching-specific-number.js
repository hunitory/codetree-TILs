const fs = require("fs");

let inputs = fs.readFileSync(0).toString().trim().split("\n").map(Number);

for ( let i = 0; i <= inputs.length - 1; i++ ) {
    if ( inputs[i] > 25 ) {
        console.log("Lower")
    } else if (inputs[i] === 25) {
        console.log("Good");
        break;
    } else {
        console.log("Higher")
    }
}