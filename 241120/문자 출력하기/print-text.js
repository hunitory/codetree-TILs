const readline = require("readline");
const rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout
})

let str;
rl.on("line", (input) => {
    str = input.trim()
}).on("close", () => {
    for (let i = 0; i <= 7 ; i++) {
        process.stdout.write(str);
    }
})