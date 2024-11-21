const readline = require("readline");
const { stdin : input, stdout : output } = require("process");

const rl = readline.createInterface({ input, output });

let inputs = [];
let ans = 0;
let cnt = 0;

rl.on("line", (input) => {
    inputs.push(Number(input));
}).on("close" , () => {
    for (let i = 0; i < 10; i ++) {
        if ( 0 <= inputs[i] && inputs[i] <= 200 ) {
            ans += inputs[i];
            cnt++;
        }
    }

    console.log(`${ans} ${(ans / cnt).toFixed(1)}`)
})