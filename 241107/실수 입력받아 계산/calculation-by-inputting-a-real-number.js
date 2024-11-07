const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

let inputs = [];
let ans = 0;


rl.on("line", (input) => {
    inputs.push(input);
}).on("close" , () => {
    inputs = inputs.map(Number);
    inputs.forEach(input => {
        ans += input
    });
    console.log(ans.toFixed(2))
})