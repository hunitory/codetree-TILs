const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let n, extent;

rl.on("line", (input) => {
    n = Number(input.trim());
    extent = n * n;
}).on("close", () => {
    if ( n < 5 ) {
        console.log(extent)
        console.log("tiny")
    } else {
        console.log(extent);
    }
});