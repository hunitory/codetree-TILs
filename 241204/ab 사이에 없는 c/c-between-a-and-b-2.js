const readline = require("readline");

const { stdin : input, stdout : output } = require("process");

const rl = readline.createInterface({ input, output });

let a = 0, b = 0, c = 0;
let flag = false;

rl.on("line", (input) => {
    [a, b, c] = input.trim().split(" ").map(Number);
}).on("close", () => {
    for ( let i = a; i <= b; i++ ) {
        if ( i % c === 0 && i / c >= 1 ) {
            flag = true;
            break
        }
    }
    if (!flag) {
        console.log("YES");
    } else {
        console.log("NO")
    }
})