const readline = require("readline");
const { stdin : input, stdout : output } = require("process");

const rl = readline.createInterface({ input, output });

let n = 0;
let flag = true;

rl.on("line", (input) => {
    n = Number(input.trim())
}).on("close", () => {
    for (let i = 2; i < n; i++ ) {
        if ( n % i === 0) {
            flag = false;
        }
    }

    if (flag === false) {
        console.log("C")
    } else {
        console.log("N")
    }
} 
)
