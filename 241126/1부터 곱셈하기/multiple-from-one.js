const readline = require("readline");

const { stdin : input, stdout : output } = require("process");

const rl = readline.createInterface({input, output});

let n = 0;
let ans = 1;

rl.on("line", (input) => {
    n = Number(input.trim());
}).on("close", () => {
    for (let i = 1; i <= 10; i++ ) {
        ans *= i
        if ( ans >= n) {
            console.log(i);
            break
        }
    }
})