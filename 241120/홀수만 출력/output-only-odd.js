const readline = require("readline");

const { stdin : input, stdout : output} = require("process");

const rl = readline.createInterface({ input, output});

let a,b;
rl.on("line", (input) => {
    [a, b] = input.trim().split(" ").map(Number)

    for (a ; a <= b ; a++) {
        if (a % 2 === 1) {
            process.stdout.write(`${a} `)
        }
    }
    rl.close();
})