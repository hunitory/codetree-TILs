const readline = require("readline");

const { stdin : input, stdout : output} = require("process");

const rl = readline.createInterface({ input, output });

let inputs = [];
let a = 0,

rl.on("line", (input) => {
    a = Number(input.trim())
    if ( a === 0 ) {
        rl.close();
    }
    inputs.push(input)
}).on("close", () => {

    for (let i = 0; i < inputs.length; i++ ){
        console.log(inputs[i])
    }
})