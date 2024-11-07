const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.output
})

rl.on("line", (input) => {
    console.log(input * 2);
    rl.close();
})