const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

let num;

rl.on("line", (input) => {
    num = input.split('-');
}).on('close', () => {
    console.log(num.join(""));
});