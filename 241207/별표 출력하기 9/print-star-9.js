const readline = require("readline");

const { stdin: input, stdout: output } = require("process");

const rl = readline.createInterface({ input, output }); 

let n = 0;
let str = "";

rl.on("line", (input) => {
    n = Number(input.trim())
}).on("close", () => {
    for (let i = 0; i < n; i++) {
        str = "";
        for (let j = 0; j + i < n - 1; j++) { 
            str += "  ";
        }
        for (let k = n * 2; k - (i * 2) - 1 < n * 2; k++) {
            str += "* "
        }

        console.log(str)
    }
})
