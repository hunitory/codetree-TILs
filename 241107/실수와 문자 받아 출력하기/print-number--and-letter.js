const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

let inputs = [];


rl.on("line", (input) => {
    inputs.push(input);
}).on("close", ()=>{
    inputs.forEach(input => {
        if (!isNaN(Number(input))) {
            input = Number(input);
            console.log(input.toFixed(2));
        } else {
            console.log(input)
        }
    })
})