const readline = require("readline");

const { stdin : input, stdout : output } = require("process");

const rl = readline.createInterface({ input, output });

let a, b;

rl.on("line", (input) => {
    [a, b] = input.trim().split(" ").map(Number);
}).on("close", () => {
    console.log(a ** b);
})