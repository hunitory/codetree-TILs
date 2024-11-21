const readline = require("readline");
const { stdin : input, stdout : output } = require("process");

const rl = readline.createInterface({ input, output });

let a, b;
let ans = 0

rl.on("line", (input) => {
    [a, b] = input.trim().split(" ").map(Number);
}).on("close", () => {
    for (a; a <= b ; a++) {
        ans += a
    }
    console.log(ans)
})