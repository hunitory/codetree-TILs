const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

let inputs = [];
let ageA, sexA, ageB, sexB;

rl.on("line", (input) => {
    inputs.push(input.trim().split(' '))
}).on("close", () => {
    [ageA, sexA] = inputs[0]; 
    [ageB, sexB] = inputs[1];

    if ((Number(ageA) >= 19 && sexA == "M") || (Number(ageB) >= 19 && sexB == "M")) {
        console.log(1)
    } else {
        console.log(0)
    }
})