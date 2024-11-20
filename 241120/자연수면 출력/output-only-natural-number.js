const readline = require("readline");
const { stdin: input, stdout: output } = require("process");

const rl = readline.createInterface({ input, output });

let a, b;

rl.on("line", (input) => {
    [a, b] = input.trim().split(" ").map(Number);
}).on("close", () => {
    if (a > 0) {
        for (let i = 0; i < b ; i ++) {
            process.stdout.write(String(a))
        }
    } else {
        console.log(0)
    }
})