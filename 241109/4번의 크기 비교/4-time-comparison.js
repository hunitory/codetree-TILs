const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output : process.stdout
})

let inputs = []

rl.on("line", (input) => {
    inputs.push(input.trim())
}).on("close", () => {
    let a = parseInt(inputs[0])
    let [b, c, d, e] = inputs[1].split(" ").map(Number)

    console.log(a > b ? 1 : 0);
    console.log(a > c ? 1 : 0);
    console.log(a > d ? 1 : 0);
    console.log(a > e ? 1 : 0);
})