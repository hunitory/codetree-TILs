const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdin
});

let num;

rl.on("line", (input) => {
    num = Number(input.trim());
}).on("close", () => {
    if (num >= 0 ) {
        console.log(num);
    } else {
        console.log(num);
        console.log('minus')
    }
})