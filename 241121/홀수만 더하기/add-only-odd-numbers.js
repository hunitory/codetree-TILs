const readline = require("readline");
const { stdin : input, stdout : output } = require("process");

const rl = readline.createInterface({ input, output });

let inputs = [];
let ans = 0;

rl.on("line", (input) => {
    inputs.push(Number(input.trim()))
}).on("close", () => {
    for (let i = 1; i <= inputs[0]; i++ ) {
        if (((inputs[i] % 2) != 0) && ((inputs[i] % 3) === 0)) {
            ans += inputs[i];
        }
    }
    console.log(ans);
})