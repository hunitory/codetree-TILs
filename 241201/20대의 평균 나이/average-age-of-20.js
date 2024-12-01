const readline = require("readline");

const { stdin : input, stdout : output } = require("process");

const rl = readline.createInterface({ input, output });

let ans = 0, cnt = 0;

rl.on("line", (input) => {
    let a = Number(input.trim())
    if (a >= 30) {
        rl.close();
    }
    ans += a
    cnt++
}).on("close", () => {
    console.log((ans / cnt).toFixed(2))
})