const readline = require("readline");

const { stdin : input, stdout : output } = require("process");

const rl = readline.createInterface({ input, output });

let n;

rl.on("line", (input) => {
    n = Number(input.trim());    
}).on("close", () => {
    for ( let i = 1; i <= n; i++ ) {
        if ( i % 2 === 0 || i % 10 === 5 || (i % 3 === 0 && i % 9 != 0) ) {
            continue
        }
        process.stdout.write(i + " ");
    }
})