const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

rl.on("line", (input) => {
    let [a, b] = input.split(" ").map(Number);

    [a, b] = [b, a];

    console.log(a, b);
})