const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

let inputs = [];

rl.on("line", (input) => {
    inputs.push(Number(input.trim()))
}).on("close", () => {
    console.log(inputs[0] + inputs[1]);
    console.log(inputs[1] % 10);
});