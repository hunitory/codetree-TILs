const readline = require("readline");

const rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout
})

let inputs = [];

rl.on("line", (input) => {
    inputs.push(input);
}).on("close", () => {
    inputs.map(Number);
    console.log(inputs[0] * inputs[1]);
});