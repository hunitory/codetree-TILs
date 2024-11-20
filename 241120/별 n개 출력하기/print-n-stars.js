const readline = require("readline");
const { stdin : input, stdout : output } = require("process");

const rl = readline.createInterface({ input, output });

let n;
rl.on("line", (input) => {
    n = Number(input.trim());
}).on("close", () => {
    let i = 1
    while ( i <= n) {
        console.log("*")
        i++
    }
})