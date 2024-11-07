const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let a, b;

rl.on("line", (input) => {
    [a, b] = input.split(" ").map(Number);
}).on("close", () => {
    console.log(a + b);
    console.log(a - b);
    console.log(Math.floor(a / b));
    console.log(a % b);
});