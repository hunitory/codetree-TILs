const readline = require("readline");

const rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout
})

let a;

rl.on("line", (input) => {
    a = Number(input.trim())
}).on("close", () => {
    console.log((10 <= a && 20 >= a) ? "yes" : "no");
})