const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

let h, m;

rl.on("line", (input) => {
    [h, m] = input.split(":").map(Number);
}).on("close", () => {
    console.log(`${h + 1}:${m}`);
})