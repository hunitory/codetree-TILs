const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

let inputs = []

rl.on("line", (input) => {
    inputs.push(...input.split(" ").map(Number))
}).on("close", () => {
    console.log(inputs.join(" "))
})