const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let n;

rl.on("line", (input) => {
    n = Number(input);
}).on("close", () => {
    if ( n >= 3000 ) {
        console.log("book");
    } else if ( n >= 1000 ) {
        console.log("mask");
    } else {
        console.log('no');
    }
})