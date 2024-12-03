const readline = require("readline");

const { stdin : input, stdout : output } = require("process");

const rl = readline.createInterface({ input, output });

let n = 0, cnt = 0;

rl.on("line", (input) => {
    n = Number(input.trim())
}).on("close", () => {
    while (n != 1) {
        n /= 2
        cnt++
    }
    console.log(cnt);
})