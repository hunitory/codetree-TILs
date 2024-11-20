const readline = require("readline");
const { stdin : input, stdout : output } = require("process");

const rl = readline.createInterface({ input, output })

let ans = 0;

rl.on("line", (input) => {
    let a = Number(input.trim())
    if (a % 2 === 1) {
        ans++
    }
}).on("close", () => {
    console.log(ans);
})