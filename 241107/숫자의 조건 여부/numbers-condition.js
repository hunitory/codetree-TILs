const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let a;

rl.on("line", (input) => {
    a = Number(input.trim());
}).on("close", () => {
    if ( a >= 113 ) {
        console.log(1);
    } else {
        console.log(0);
    }
})