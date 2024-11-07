const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let score;

rl.on("line", (input) => {
    score = Number(input.trim());
    score === 100 ? console.log("pass") : console.log("failure");
    rl.close();
})