const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

let a, b ;

rl.on("line", (input) => {
    [a, b] = input.trim().split(" ").map(Number);
}).on("close", () => {
    console.log(((a + b) / (a - b)).toFixed(2));
})