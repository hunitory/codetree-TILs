const readline = require("readline");

const rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout
})

let a;

rl.on("line", (input) => {
    a = Number(input.trim())
    if (a % 13 == 0 || a % 19 == 0) {
        console.log('True');
    } else {
        console.log("False");
    }
    rl.close()
})