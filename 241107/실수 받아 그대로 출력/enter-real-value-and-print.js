const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

rl.on("line", (num) => {
    num = Number(num);
    console.log(num.toFixed(2));
    rl.close();
});