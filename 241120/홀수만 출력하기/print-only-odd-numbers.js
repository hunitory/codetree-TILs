const fs = require("fs");

let inputs = fs.readFileSync(0).toString().trim().split('\n').map(Number);

for ( let i = 1; i <= inputs[0]; i++ ) {
    if (inputs[i] % 3 === 0 && inputs[i] % 2 === 1) {
        console.log(inputs[i])
    } 
}