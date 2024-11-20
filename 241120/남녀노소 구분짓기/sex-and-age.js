const readline = require("readline");
const { stdin : input, stdout : output } = require("process");

const rl = readline.createInterface({ input , output })

let inputs = [];

rl.on("line", (input) => {
    inputs.push(Number(input));
}).on("close" , () => {
    if (inputs[0] == 0) {
        if (inputs[1] >= 19 ) {
            console.log("MAN")
        } else {
            console.log("BOY")
        }
    } else {
        if (inputs[1] >= 19 ) {
            console.log("WOMAN")
        } else {
            console.log("GIRL")
        }
    }
})