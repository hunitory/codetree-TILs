const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let water;

rl.on("line", (input) => {
    water = Number(input);
}).on('close', () => {
    if (water >= 100) {
        console.log('vapor');
    } else if (water >= 0) {
        console.log('water');
    } else {
        console.log('ice');
    }
});