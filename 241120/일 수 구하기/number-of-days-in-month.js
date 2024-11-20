const readline = require("readline");

const { stdin : input, stdout : output } = require("process");

const rl = readline.createInterface({
    input,
    output
})

let n;

rl.on("line", (input) => {
    n = Number(input.trim())
}).on("close", () => {
    if (n === 2) {
        console.log(28);
    } else if (n <= 7){
        if ( n % 2 === 1) {
            console.log(31)
        } else {
            console.log(30)
        }
    } else {
        if (n % 2 === 0) {
            console.log(31);
        } else {
            console.log(30);
        }
    }
})