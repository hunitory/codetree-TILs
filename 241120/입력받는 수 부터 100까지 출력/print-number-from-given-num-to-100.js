const readline = require("readline");
const { stdin : input, stdout : output } = require("process");

const rl = readline.createInterface({input, output});

let n;

rl.on("line" , (input) => {
    n = Number(input.trim())
}).on("close", () => {
    for (n; n <= 100; n++) {
        process.stdout.write(n + " ");
    }
})