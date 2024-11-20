const readline = require("readline");

const { stdin : input, stdout : output} = require("process");

const rl = readline.createInterface({
    input, output
});

let c, n;

rl.on("line", (input) => {
    let inputs = input.trim().split(" ")
    c = inputs[0];
    n = Number(inputs[1]);
}).on("close", () => {
    if (c === "A") {
        for (let i = 1; i <= n ; i++ ) {
            process.stdout.write(`${i} `);
        }
    } else {
        for (let i = 0; i < n ; i++ ) {
            process.stdout.write(`${n - i} `);
        }
    }
})