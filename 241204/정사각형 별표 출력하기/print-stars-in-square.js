const readline = require("readline");

const { stdin : input, stdout : output } = require("process");

const rl = readline.createInterface({ input, output });

let n = 0;

rl.on("line", (input) => {
    n = Number(input.trim())
}).on("close", () => {
    for (let i = 0; i < n; i++ ) {
        for (let j = 0 ; j < n; j++ ){
            process.stdout.write('*' + "");
        }
        console.log();
    }
})