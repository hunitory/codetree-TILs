const readline = require("readline");
const rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout
})

let a,b;

rl.on("line", (input) => {
    [a, b] = input.trim().split(" ").map(Number);
}).on('close', () => {
    while (a <= b) {
        if (a % 2 === 0){
            process.stdout.write(`${a} `)
        }
        a++
    }
})