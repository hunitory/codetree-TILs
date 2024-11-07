const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    ouput: process.stdout
})

let a, b, c;

rl.on("line", (input) => {
    [a, b, c] = input.trim().split(" ").map(Number);
}).on("close", () => {
    console.log(a + b + c);
    console.log(Math.floor((a + b + c) / 3));
})