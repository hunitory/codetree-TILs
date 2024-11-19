const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

let ageA, sexA, ageB, sexB;

rl.on("line", (input) => {
    [ageA, sexA] = input.trim().split(' ')
    [ageB, sexB] = input.trim().split(' ')

    if ((Number(ageA) >= 19 && sexA == "M") || (Number(ageB) >= 19 && sexB == "M") ) {
        console.log(1)
    } else {
        console.log(0)
    }
    rl.close()
})